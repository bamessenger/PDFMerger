from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject


class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.InsertInto_Label = QtWidgets.QLabel(self.centralwidget)
        self.InsertInto_Label.setGeometry(QtCore.QRect(29, 250, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.InsertInto_Label.setFont(font)
        self.InsertInto_Label.setObjectName("InsertInto_Label")
        self.Title_Label = QtWidgets.QLabel(self.centralwidget)
        self.Title_Label.setGeometry(QtCore.QRect(9, 1, 331, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(78, 143, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 143, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.Title_Label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Title_Label.setFont(font)
        self.Title_Label.setObjectName("Title_Label")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(29, 770, 841, 101))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.hide()
        self.progressBar = QtWidgets.QProgressBar(self.frame_3)
        self.progressBar.setGeometry(QtCore.QRect(37, 50, 791, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progress_label = QtWidgets.QLabel(self.frame_3)
        self.progress_label.setGeometry(QtCore.QRect(4, 20, 831, 21))
        self.progress_label.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_label.setObjectName("progressBar_label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(29, 290, 841, 421))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(3)
        self.frame_2.setMidLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.BrowseFileInsertInto_Label = QtWidgets.QLabel(self.frame_2)
        self.BrowseFileInsertInto_Label.setGeometry(
            QtCore.QRect(14, 50, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BrowseFileInsertInto_Label.setFont(font)
        self.BrowseFileInsertInto_Label.setObjectName(
            "BrowseFileInsertInto_Label")
        self.BrowseFileInsertInto = QtWidgets.QPushButton(self.frame_2)
        self.BrowseFileInsertInto.setGeometry(QtCore.QRect(700, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BrowseFileInsertInto.setFont(font)
        self.BrowseFileInsertInto.setObjectName("BrowseFileInsertInto")
        self.InsertAfterPageNum_Label = QtWidgets.QLabel(self.frame_2)
        self.InsertAfterPageNum_Label.setGeometry(
            QtCore.QRect(16, 342, 221, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.InsertAfterPageNum_Label.setFont(font)
        self.InsertAfterPageNum_Label.setObjectName("InsertAfterPageNum_Label")
        self.InsertEveryNthPageNum_Label = QtWidgets.QLabel(self.frame_2)
        self.InsertEveryNthPageNum_Label.setGeometry(
            QtCore.QRect(339, 342, 211, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.InsertEveryNthPageNum_Label.setFont(font)
        self.InsertEveryNthPageNum_Label.setObjectName(
            "InsertEveryNthPageNum_Label")
        self.InsertAfterPageNum = QtWidgets.QSpinBox(self.frame_2)
        self.InsertAfterPageNum.setGeometry(QtCore.QRect(241, 342, 66, 30))
        self.InsertAfterPageNum.setMaximum(9999)
        self.InsertAfterPageNum.setObjectName("InsertAfterPageNum")
        self.InsertEveryNthPageNum = QtWidgets.QSpinBox(self.frame_2)
        self.InsertEveryNthPageNum.setGeometry(QtCore.QRect(541, 342, 66, 30))
        self.InsertEveryNthPageNum.setMaximum(9999)
        self.InsertEveryNthPageNum.setObjectName("InsertEveryNthPageNum")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setGeometry(QtCore.QRect(149, 49, 531, 281))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 529, 279))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.FileNamesInsertInto = QtWidgets.QTextEdit(
            self.scrollAreaWidgetContents)
        self.FileNamesInsertInto.setGeometry(QtCore.QRect(-1, -1, 571, 281))
        self.FileNamesInsertInto.setObjectName("FileNamesInsertInto")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(29, 110, 841, 111))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName("frame")
        self.FileNameCopy = QtWidgets.QLineEdit(self.frame)
        self.FileNameCopy.setGeometry(QtCore.QRect(150, 39, 531, 31))
        self.FileNameCopy.setText("")
        self.FileNameCopy.setClearButtonEnabled(False)
        self.FileNameCopy.setObjectName("FileNameCopy")
        self.BrowseFileCopy_Label = QtWidgets.QLabel(self.frame)
        self.BrowseFileCopy_Label.setGeometry(QtCore.QRect(14, 39, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BrowseFileCopy_Label.setFont(font)
        self.BrowseFileCopy_Label.setObjectName("BrowseFileCopy_Label")
        self.BrowseFileCopy = QtWidgets.QPushButton(self.frame)
        self.BrowseFileCopy.setGeometry(QtCore.QRect(700, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BrowseFileCopy.setFont(font)
        self.BrowseFileCopy.setObjectName("BrowseFileCopy")
        self.CopyFrom_Label = QtWidgets.QLabel(self.centralwidget)
        self.CopyFrom_Label.setGeometry(QtCore.QRect(29, 70, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.CopyFrom_Label.setFont(font)
        self.CopyFrom_Label.setObjectName("CopyFrom_Label")
        self.ExecuteButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExecuteButton.setGeometry(QtCore.QRect(398, 730, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ExecuteButton.setFont(font)
        self.ExecuteButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExecuteButton.setObjectName("ExecuteButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Merge PDF\'s"))
        self.InsertInto_Label.setText(
            _translate("MainWindow", "PDF File(s) (insert into):"))
        self.Title_Label.setText(_translate("MainWindow", "PDFMerger"))
        self.progress_label.setText(
            _translate("MainWindow", " "))
        self.BrowseFileInsertInto_Label.setText(
            _translate("MainWindow", "File Name(s):"))
        self.BrowseFileInsertInto.setText(_translate("MainWindow", "Browse"))
        self.InsertAfterPageNum_Label.setText(
            _translate("MainWindow", "Start Insert "
                                     "AFTER Page:"))
        self.InsertEveryNthPageNum_Label.setText(
            _translate("MainWindow", "Insert Every "
                                     "nth Page:"))
        self.BrowseFileCopy_Label.setText(
            _translate("MainWindow", "File Name:"))
        self.BrowseFileCopy.setText(_translate("MainWindow", "Browse"))
        self.CopyFrom_Label.setText(
            _translate("MainWindow", "PDF File (copy from):"))
        self.ExecuteButton.setText(_translate("MainWindow", "Execute"))
