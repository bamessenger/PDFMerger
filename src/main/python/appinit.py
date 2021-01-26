from PyQt5.QtCore import QRunnable
from PyQt5.QtWidgets import QFileDialog, QListView, QTreeView, \
    QAbstractItemView, QDialog
from PyQt5 import QtWidgets

from userinterface import Ui_MainWindow
from pdfmerge import ExecutePDF

class Worker(QRunnable):
    def __init__(self):
        super().__init__()

class MainWindowUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindowUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.executepdf = ExecutePDF()
        self.copyFromFile = None
        self.insertIntoFiles = None

        self.ui.frame_3.hide()
        self.ui.BrowseFileCopy.clicked.connect(self.browseCopyFrom)
        self.ui.BrowseFileInsertInto.clicked.connect(self.browseInsertInto)
        self.ui.ExecuteButton.clicked.connect(self.execute)

    def browseCopyFrom(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.copyFromFile, _ = QtWidgets.QFileDialog.getOpenFileName(None,
                                                                 "Open", "",
                                                            "All Files ("
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

    def execute(self):
        self.executepdf.merge(self.copyFromFile,
                              self.insertIntoFiles,
                              self.ui.InsertAfterPageNum.value(),
                              self.ui.InsertEveryNthPageNum.value())