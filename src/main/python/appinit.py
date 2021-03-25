from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import QFileDialog, QListView, QTreeView, \
    QAbstractItemView, QDialog, QMessageBox
from PyQt5 import QtWidgets
from userinterface import Ui_MainWindow
from worker import WorkerManager, Worker


class MainWindowUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindowUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.msgBox = QMessageBox()
        self.ui.setupUi(self)
        self.threadpool = QThreadPool()
        self.worker = WorkerManager()
        # Connect button signals to slots
        self.ui.BrowseFileCopy.clicked.connect(self.browseCopyFrom)
        self.ui.BrowseFileInsertInto.clicked.connect(self.browseInsertInto)
        self.ui.ExecuteButton.clicked.connect(self.startWorker)

    def browseCopyFrom(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.copyFromFile, _ = QtWidgets.QFileDialog.getOpenFileName(None,
                                                                     "Open", "",
                                                                     "All "
                                                                     "Files ("
                                                                     "*);;Python Files "
                                                                     "(*.py)",
                                                                     options=options)
        if self.copyFromFile:
            self.ui.FileNameCopy.setText(self.copyFromFile)

    def browseInsertInto(self):
        multiSelect = QFileDialog()
        multiSelect.setOption(multiSelect.DontUseNativeDialog, True)
        multiSelect.setOption(multiSelect.HideNameFilterDetails, True)
        multiSelect.setOption(multiSelect.ShowDirsOnly, False)
        multiSelect.findChildren(QListView)[0].setSelectionMode(
            QAbstractItemView.ExtendedSelection)
        multiSelect.findChildren(QTreeView)[0].setSelectionMode(
            QAbstractItemView.ExtendedSelection)
        if multiSelect.exec_() == QDialog.Accepted:
            self.insertIntoFiles = multiSelect.selectedFiles()
            # clear out any old selections
            self.ui.FileNamesInsertInto.clear()
            # loop through all files selected and add to screen
            for file in range(len(self.insertIntoFiles)):
                self.ui.FileNamesInsertInto.append(self.insertIntoFiles[file])

    def startProc(self):
        self.ui.frame_3.show()
        self.ui.progress_label.setText("Merging in Progress...")

    def progressProc(self, val):
        percent = val / self.files
        self.ui.progressBar.setValue(percent)

    def completedProc(self):
        self.showCompletion()
        self.ui.frame_3.hide()

    def showCompletion(self):
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText("Merge Completed Successfully")
        self.msgBox.setWindowTitle("Program Status")
        self.msgBox.setStandardButtons(QMessageBox.Ok)
        self.msgBox.exec()

    def startWorker(self):
        self.files = len(self.insertIntoFiles)
        self.worker.signals.completed.connect(self.completedProc)
        self.worker.signals.progress.connect(self.progressProc)
        for file in range(self.files):
            w = Worker(self.copyFromFile, self.insertIntoFiles[file],
                                 self.ui.InsertAfterPageNum.value(),
                                 self.ui.InsertEveryNthPageNum.value())
            w.signals.started.connect(self.startProc)
            self.worker.enqueue(w)