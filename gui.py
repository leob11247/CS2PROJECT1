# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Voter_ID = QtWidgets.QLabel(parent=self.centralwidget)
        self.Voter_ID.setGeometry(QtCore.QRect(20, 80, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Voter_ID.setFont(font)
        self.Voter_ID.setObjectName("Voter_ID")
        self.id_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.id_input.setGeometry(QtCore.QRect(140, 80, 121, 21))
        self.id_input.setObjectName("id_input")
        self.Welcome_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Welcome_label.setGeometry(QtCore.QRect(160, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Welcome_label.setFont(font)
        self.Welcome_label.setObjectName("Welcome_label")
        self.candidate_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.candidate_label.setGeometry(QtCore.QRect(140, 140, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.candidate_label.setFont(font)
        self.candidate_label.setObjectName("candidate_label")
        self.Joh_Button = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.Joh_Button.setGeometry(QtCore.QRect(160, 210, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Joh_Button.setFont(font)
        self.Joh_Button.setObjectName("Joh_Button")
        self.Candidate_Group = QtWidgets.QButtonGroup(MainWindow)
        self.Candidate_Group.setObjectName("Candidate_Group")
        self.Candidate_Group.addButton(self.Joh_Button)
        self.Jane_radio = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.Jane_radio.setGeometry(QtCore.QRect(160, 260, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Jane_radio.setFont(font)
        self.Jane_radio.setObjectName("Jane_radio")
        self.Candidate_Group.addButton(self.Jane_radio)
        self.submit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(110, 320, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")
        self.detail_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.detail_label.setGeometry(QtCore.QRect(50, 400, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.detail_label.setFont(font)
        self.detail_label.setObjectName("detail_label")
        self.results_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.results_button.setGeometry(QtCore.QRect(350, 320, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.results_button.setFont(font)
        self.results_button.setObjectName("results_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voting Form"))
        self.Voter_ID.setText(_translate("MainWindow", "Voter ID:"))
        self.Welcome_label.setText(_translate("MainWindow", "Welcome!"))
        self.candidate_label.setText(_translate("MainWindow", "Candidates"))
        self.Joh_Button.setText(_translate("MainWindow", "John"))
        self.Jane_radio.setText(_translate("MainWindow", "Jane"))
        self.submit_button.setText(_translate("MainWindow", "Submit Vote"))
        self.detail_label.setText(_translate("MainWindow", "Please Choose One Candidate!"))
        self.results_button.setText(_translate("MainWindow", "See Results"))
