import math
import os.path
import uuid

from pdfrw import PdfWriter, PdfReader
from PyQt5.QtCore import pyqtSignal, QRunnable, QObject, QThreadPool


class WorkerSignals(QObject):
    # Create worker signals
    started = pyqtSignal(str)
    progress = pyqtSignal(int)
    finished = pyqtSignal(str)
    completed = pyqtSignal()

class WorkerManager(QObject):

    _workers = {}

    def __init__(self):
        super().__init__()

        # Create a threadpool for workers.
        self.threadpool = QThreadPool()
        self.signals = WorkerSignals()

    def enqueue(self, worker):
        worker.signals.finished.connect(self.notifyCompletion)
        self.threadpool.start(worker)
        self._workers[worker.jobID] = worker

    def notifyCompletion(self, jobID):
        self._workers[jobID] = 'Complete'
        num = sum(x == 'Complete' for x in self._workers.values())
        val = num * 100
        self.signals.progress.emit(val)
        if all(x == 'Complete' for x in self._workers.values()):
            self.signals.completed.emit()

class Worker(QRunnable):
    def __init__(self, fileCopy, fileInsInto, pageStart, pageIteration):
        super().__init__()
        self.pageStart = pageStart
        self.fileCopy = fileCopy
        self.page = self.pageStart - 1
        self.pages = 0
        self.pageIterate = pageIteration
        self.currentPage = 0
        self.writer = PdfWriter()
        self.fileInsInto = fileInsInto
        # create unique identifier for each worker
        self.jobID = str(uuid.uuid4().hex)
        self.signals = WorkerSignals()

    def run(self):
        self.signals.started.emit(self.jobID)
        self.fPath = PdfReader(self.fileInsInto)
        outfn = os.path.splitext(self.fileInsInto)[0] + "_MERGED.pdf"
        copyFrom_totalPages = len(PdfReader(self.fileCopy).pages)
        # Calculate the total pages for the current fileInsertInto file
        insInto_totalPages = len(self.fPath.pages)
        # Calculate total number of pages upon merging...round up to nearest
        # whole number
        self.totalPages = math.ceil((
                insInto_totalPages + ((
                insInto_totalPages - self.pageStart) / self.pageIterate) *
                copyFrom_totalPages))
        while self.pages < self.totalPages:
            if self.pages == self.page:
                self.writer.addpages(PdfReader(self.fileCopy).pages)
                self.page += self.pageIterate
                self.pages += copyFrom_totalPages
            else:
                self.writer.addpage(self.fPath.pages[self.currentPage])
                self.currentPage += 1
                self.pages += 1
        # Write all the files into a file which is named as shown below
        # File directory is that of the last insert into file chosen
        self.writer.write(outfn)
        self.signals.finished.emit(self.jobID)
