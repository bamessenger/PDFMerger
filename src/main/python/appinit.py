from PyQt5.QtCore import QRunnable, QThreadPool, pyqtSlot
from PyQt5.QtWidgets import QFileDialog, QListView, QTreeView, \
    QAbstractItemView, QDialog, QMessageBox
from PyQt5 import QtWidgets
from userinterface import Ui_MainWindow
from pdfmerge import ExecutePDF


class Worker(QRunnable):
    def __init__(self, copy, insert, pgstart, pgiter):
        super(Worker, self).__init__()
        self.executepdf = ExecutePDF()
        self.copy = copy
        self.insert = insert
        self.pgstart = pgstart
        self.pgiter = pgiter

    def run(self):
        self.executepdf.merge(self.copy, self.insert, self.pgstart, self.pgiter)


class MainWindowUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindowUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.msgBox = QMessageBox()
        self.ui.setupUi(self)
        self.threadpool = QThreadPool()
        self.hideFrame3()
        # Connect button signals to slots
        self.ui.BrowseFileCopy.clicked.connect(self.browseCopyFrom)
        self.ui.BrowseFileInsertInto.clicked.connect(self.browseInsertInto)
        self.ui.ExecuteButton.clicked.connect(self.execute)
        self.ui.ExecuteButton.clicked.connect(self.showFrame3)

    @pyqtSlot()
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

    @pyqtSlot()
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

    @pyqtSlot()
    def execute(self):
        self.worker = Worker(self.copyFromFile, self.insertIntoFiles,
                             self.ui.InsertAfterPageNum.value(),
                             self.ui.InsertEveryNthPageNum.value())
        self.threadpool.start(self.worker)
        # call message box after successful completion
        if self.threadpool.waitForDone():
            self.showCompletion()

    def showCompletion(self):
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText("Merge Completed Successfully")
        self.msgBox.setWindowTitle("Program Status")
        self.msgBox.setStandardButtons(QMessageBox.Ok)

        self.msgBox.exec()

    @pyqtSlot()
    def showFrame3(self):
        self.ui.frame_3.show()

    def hideFrame3(self):
        self.ui.frame_3.hide()
