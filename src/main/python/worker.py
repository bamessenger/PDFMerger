import math
import os.path

from pdfrw import PdfWriter, PdfReader
from PyQt5.QtCore import QObject, pyqtSignal


class Worker(QObject):
    # Create worker signals
    start = pyqtSignal()
    progress = pyqtSignal(int)
    finished = pyqtSignal()
    def __init__(self, fileCopy, fileInsertInto, pageStart, pageIteration):
        super().__init__()
        self.pageStart = pageStart
        self.fileCopy = fileCopy
        self.fileInsertInto = fileInsertInto
        self.page = self.pageStart - 1
        self.pages = 0
        self.pageIterate = pageIteration
        self.cnt = 0
        self.currentPage = 0
        self.readerCopy = PdfReader(self.fileCopy)
        self.writer = PdfWriter()

    def run(self):
        self.start.emit()
        copyFrom_totalPages = len(PdfReader(self.fileCopy).pages)
        # Loop through each file chosen by user
        for files in range(len(self.fileInsertInto)):
            # Read object for fileInsertInto file(s)
            readerIns = PdfReader(self.fileInsertInto[files])
            # Calculate the total pages for the current fileInsertInto file
            insInto_totalPages = len(PdfReader(self.fileInsertInto[
                                                   files]).pages)
            # Calculate total number of pages upon merging...round up to nearest
            # whole number
            totalPages = math.ceil((insInto_totalPages + ((insInto_totalPages
                                                           - self.pageStart) /
                                                          self.pageIterate) *
                                    copyFrom_totalPages))
            while self.pages < totalPages:
                if self.pages == self.page:
                    self.writer.addpages(self.readerCopy.pages)
                    self.page += self.pageIterate
                    self.pages += copyFrom_totalPages
                else:
                    self.writer.addpage(readerIns.pages[self.currentPage])
                    self.currentPage += 1
                    self.pages += 1
                while self.cnt < 100:
                    self.cnt = self.cnt + (1/len(self.fileInsertInto))
                    self.progress.emit(self.cnt)
            # Write all the files into a file which is named as shown below
            # File directory is that of the last insert into file chosen
            directory = os.path.dirname(self.fileInsertInto[-1])
            self.writer.write(
                os.path.splitext(self.fileInsertInto[files])[0] + "_MERGED.pdf")
        self.finished.emit()
