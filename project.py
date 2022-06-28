from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from static.MusicalNotes import Notes
from static.stylesheet import stylesheetclass
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1125, 754)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1091, 581))
        self.frame.setStyleSheet("border-image:url(/static/pexels-rok-romih-3848158.jpg);\n""border-radius:20px;\n")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 1091, 581))
        self.frame_2.setStyleSheet("background-color: rgb(0, 0, 0,125);\n""border-radius:20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_C = QtWidgets.QPushButton(Form)
        self.pushButton_C.setGeometry(QtCore.QRect(50, 220, 51, 321))
        self.pushButton_C.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_C.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_C.setFont(font)
        self.pushButton_C.setStyleSheet(stylesheetclass.stylesWhite(self))
        self.pushButton_C.setObjectName("pushButton_C")
        self.pushButton_C.clicked.connect(Notes.C)
        self.pushButton_D = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_D.setGeometry(QtCore.QRect(100, 210, 51, 321))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_D.setFont(font)
        self.pushButton_D.setStyleSheet(stylesheetclass.stylesWhite(self))
        self.pushButton_D.setObjectName("pushButton_D")
        self.pushButton_D.clicked.connect(Notes.D)
        self.pushButton_E = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_E.setGeometry(QtCore.QRect(160, 210, 51, 321))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_E.setFont(font)
        self.pushButton_E.setStyleSheet(stylesheetclass.stylesWhite(self))
        self.pushButton_E.setObjectName("pushButton_E")
        self.pushButton_E.clicked.connect(Notes.E)
        self.pushButton_F = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_F.setGeometry(QtCore.QRect(220, 210, 51, 321))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_F.setFont(font)
        self.pushButton_F.setStyleSheet(stylesheetclass.stylesWhite(self))
        self.pushButton_F.setObjectName("pushButton_F")
        self.pushButton_F.clicked.connect(Notes.F)
        self.pushButton_G = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_G.setGeometry(QtCore.QRect(280, 210, 51, 321))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_G.setFont(font)
        self.pushButton_G.setStyleSheet(stylesheetclass.stylesWhite(self))
        self.pushButton_G.setObjectName("pushButton_G")
        self.pushButton_G.clicked.connect(Notes.G)
        self.pushButton_B = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_B.setGeometry(QtCore.QRect(400, 210, 51, 321))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_B.setFont(font)
        self.pushButton_B.setStyleSheet(stylesheetclass.stylesWhite(self))
        self.pushButton_B.setObjectName("pushButton_B")
        self.pushButton_B.clicked.connect(Notes.B)
        self.pushButton_C2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_C2.setGeometry(QtCore.QRect(460, 210, 51, 321))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_C2.setFont(font)
        self.pushButton_C2.setStyleSheet(stylesheetclass.stylesWhite(self))
        self.pushButton_C2.setObjectName("pushButton_C2")
        self.pushButton_C2.clicked.connect(Notes.C2)
        self.pushButton_D2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_D2.setGeometry(QtCore.QRect(520, 210, 51, 321))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_D2.setFont(font)
        self.pushButton_D2.setStyleSheet(stylesheetclass.stylesWhite(self))
        self.pushButton_D2.setObjectName("pushButton_D2")
        self.pushButton_D2.clicked.connect(Notes.D2)
        self.pushButton_E2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_E2.setGeometry(QtCore.QRect(580, 210, 51, 321))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_E2.setFont(font)
        self.pushButton_E2.setStyleSheet(stylesheetclass.stylesWhite(self))
        self.pushButton_E2.setObjectName("pushButton_E2")
        self.pushButton_E2.clicked.connect(Notes.E2)
        self.pushButton_F2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_F2.setGeometry(QtCore.QRect(640, 210, 51, 321))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_F2.setFont(font)
        self.pushButton_F2.setStyleSheet(stylesheetclass.stylesWhite(self))
        self.pushButton_F2.setObjectName("pushButton_F2")
        self.pushButton_F2.clicked.connect(Notes.F2)
        self.pushButton_G2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_G2.setGeometry(QtCore.QRect(700, 210, 51, 321))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_G2.setFont(font)
        self.pushButton_G2.setStyleSheet(stylesheetclass.stylesWhite(self))
        self.pushButton_G2.setObjectName("pushButton_G2")
        self.pushButton_G2.clicked.connect(Notes.G2)
        self.pushButton_B2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_B2.setGeometry(QtCore.QRect(820, 210, 51, 321))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_B2.setFont(font)
        self.pushButton_B2.setStyleSheet(stylesheetclass.stylesWhite(self))
        self.pushButton_B2.setObjectName("pushButton_B2")
        self.pushButton_B2.clicked.connect(Notes.B2)
        self.pushButton_C3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_C3.setGeometry(QtCore.QRect(880, 210, 51, 321))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_C3.setFont(font)
        self.pushButton_C3.setStyleSheet(stylesheetclass.stylesWhite(self))
        self.pushButton_C3.setObjectName("pushButton_C3")
        self.pushButton_C3.clicked.connect(Notes.C3)
        self.pushButton_E3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_E3.setGeometry(QtCore.QRect(1000, 210, 51, 321))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_E3.setFont(font)
        self.pushButton_E3.setStyleSheet(stylesheetclass.stylesWhite(self))
        self.pushButton_E3.setObjectName("pushButton_E3")
        self.pushButton_E3.clicked.connect(Notes.E3)
        self.pushButton_A = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_A.setGeometry(QtCore.QRect(340, 210, 51, 321))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_A.setFont(font)
        self.pushButton_A.setStyleSheet(stylesheetclass.stylesWhite(self))
        self.pushButton_A.setObjectName("pushButton_A")
        self.pushButton_A.clicked.connect(Notes.A)
        self.pushButton_A2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_A2.setGeometry(QtCore.QRect(760, 210, 51, 321))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_A2.setFont(font)
        self.pushButton_A2.setStyleSheet(stylesheetclass.stylesWhite(self))
        self.pushButton_A2.setObjectName("pushButton_A2")
        self.pushButton_A2.clicked.connect(Notes.A2)
        self.pushButton_D3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_D3.setGeometry(QtCore.QRect(940, 210, 51, 321))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_D3.setFont(font)
        self.pushButton_D3.setStyleSheet(stylesheetclass.stylesWhite(self))
        self.pushButton_D3.setObjectName("pushButton_3")
        self.pushButton_D3.clicked.connect(Notes.D3)
        self.pushButton_Chasz = QtWidgets.QPushButton(Form)
        self.pushButton_Chasz.setGeometry(QtCore.QRect(90, 222, 31, 161))
        self.pushButton_Chasz.setStyleSheet(stylesheetclass.stylesBlack(self))
        self.pushButton_Chasz.setObjectName("pushButton_Chasz")
        self.pushButton_Chasz.clicked.connect(Notes.Csharp)
        self.pushButton_Dhasz = QtWidgets.QPushButton(Form)
        self.pushButton_Dhasz.setGeometry(QtCore.QRect(150, 220, 31, 161))
        self.pushButton_Dhasz.setStyleSheet(stylesheetclass.stylesBlack(self))
        self.pushButton_Dhasz.setObjectName("pushButton_Dhasz")
        self.pushButton_Dhasz.clicked.connect(Notes.Dsharp)
        self.pushButton_Fhasz = QtWidgets.QPushButton(Form)
        self.pushButton_Fhasz.setGeometry(QtCore.QRect(270, 220, 31, 161))
        self.pushButton_Fhasz.setStyleSheet(stylesheetclass.stylesBlack(self))
        self.pushButton_Fhasz.setObjectName("pushButton_Fhasz")
        self.pushButton_Fhasz.clicked.connect(Notes.Fsharp)
        self.pushButton_Ghasz = QtWidgets.QPushButton(Form)
        self.pushButton_Ghasz.setGeometry(QtCore.QRect(330, 220, 31, 161))
        self.pushButton_Ghasz.setStyleSheet(stylesheetclass.stylesBlack(self))
        self.pushButton_Ghasz.setObjectName("pushButton_Ghasz")
        self.pushButton_Ghasz.clicked.connect(Notes.Gsharp)
        self.pushButton_Ahasz = QtWidgets.QPushButton(Form)
        self.pushButton_Ahasz.setGeometry(QtCore.QRect(390, 220, 31, 161))
        self.pushButton_Ahasz.setStyleSheet(stylesheetclass.stylesBlack(self))
        self.pushButton_Ahasz.setObjectName("pushButton_Ahasz")
        self.pushButton_Ahasz.clicked.connect(Notes.Asharp)
        self.pushButton_Chasz2 = QtWidgets.QPushButton(Form)
        self.pushButton_Chasz2.setGeometry(QtCore.QRect(510, 220, 31, 161))
        self.pushButton_Chasz2.setStyleSheet(stylesheetclass.stylesBlack(self))
        self.pushButton_Chasz2.setObjectName("pushButton_Chasz2")
        self.pushButton_Chasz2.clicked.connect(Notes.Csharp2)
        self.pushButton_Dhasz2 = QtWidgets.QPushButton(Form)
        self.pushButton_Dhasz2.setGeometry(QtCore.QRect(570, 220, 31, 161))
        self.pushButton_Dhasz2.setStyleSheet(stylesheetclass.stylesBlack(self))
        self.pushButton_Dhasz2.setObjectName("pushButton_Dhasz2")
        self.pushButton_Dhasz2.clicked.connect(Notes.Dsharp2)
        self.pushButton_Fhasz2 = QtWidgets.QPushButton(Form)
        self.pushButton_Fhasz2.setGeometry(QtCore.QRect(690, 220, 31, 161))
        self.pushButton_Fhasz2.setStyleSheet(stylesheetclass.stylesBlack(self))
        self.pushButton_Fhasz2.setObjectName("pushButton_Fhasz2")
        self.pushButton_Fhasz2.clicked.connect(Notes.Fsharp2)
        self.pushButton_Ghasz2 = QtWidgets.QPushButton(Form)
        self.pushButton_Ghasz2.setGeometry(QtCore.QRect(750, 220, 31, 161))
        self.pushButton_Ghasz2.setStyleSheet(stylesheetclass.stylesBlack(self))
        self.pushButton_Ghasz2.setObjectName("pushButton_Ghasz2")
        self.pushButton_Ghasz2.clicked.connect(Notes.Gsharp2)
        self.pushButton_Ahasz2 = QtWidgets.QPushButton(Form)
        self.pushButton_Ahasz2.setGeometry(QtCore.QRect(810, 220, 31, 161))
        self.pushButton_Ahasz2.setStyleSheet(stylesheetclass.stylesBlack(self))
        self.pushButton_Ahasz2.setObjectName("pushButton_Ahasz2")
        self.pushButton_Ahasz2.clicked.connect(Notes.Asharp2)
        self.pushButton_Chasz3 = QtWidgets.QPushButton(Form)
        self.pushButton_Chasz3.setGeometry(QtCore.QRect(930, 220, 31, 161))
        self.pushButton_Chasz3.setStyleSheet(stylesheetclass.stylesBlack(self))
        self.pushButton_Chasz3.setObjectName("pushButton_Chasz3")
        self.pushButton_Chasz3.clicked.connect(Notes.Csharp3)
        self.pushButton_Dhasz3 = QtWidgets.QPushButton(Form)
        self.pushButton_Dhasz3.setGeometry(QtCore.QRect(990, 220, 31, 161))
        self.pushButton_Dhasz3.setStyleSheet(stylesheetclass.stylesBlack(self))
        self.pushButton_Dhasz3.setObjectName("pushButton_Dhasz3")
        self.pushButton_Dhasz3.clicked.connect(Notes.Dsharp3)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(1040, 20, 51, 41))
        font = QtGui.QFont()
        font.setFamily("font bottons music")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(stylesheetclass.stylesCloseIcon(self))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:sys.exit())
        self.labelPianoApp = QtWidgets.QLabel(Form)
        self.labelPianoApp.setGeometry(QtCore.QRect(20, 39, 1071, 121))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.labelPianoApp.setFont(font)
        self.labelPianoApp.setStyleSheet("color:white;")
        self.labelPianoApp.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPianoApp.setObjectName("labelPianoApp")
        self.label_JakubKielb = QtWidgets.QLabel(Form)
        self.label_JakubKielb.setGeometry(QtCore.QRect(20, 150, 1071, 61))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_JakubKielb.setFont(font)
        self.label_JakubKielb.setStyleSheet("color:white;")
        self.label_JakubKielb.setAlignment(QtCore.Qt.AlignCenter)
        self.label_JakubKielb.setObjectName("label_JakubKielb")
        self.frame.raise_()
        self.frame_2.raise_()
        self.pushButton_Dhasz.raise_()
        self.pushButton_Chasz2.raise_()
        self.pushButton_Dhasz2.raise_()
        self.pushButton_Fhasz2.raise_()
        self.pushButton_C.raise_()
        self.pushButton_Chasz.raise_()
        self.pushButton_Ahasz.raise_()
        self.pushButton_Ghasz.raise_()
        self.pushButton_Fhasz.raise_()
        self.pushButton_Ghasz2.raise_()
        self.pushButton_Ahasz2.raise_()
        self.pushButton_Chasz3.raise_()
        self.pushButton_Dhasz3.raise_()
        self.labelPianoApp.raise_()
        self.label_JakubKielb.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_D.setText(_translate("Form", "D"))
        self.pushButton_E.setText(_translate("Form", "E"))
        self.pushButton_F.setText(_translate("Form", "F"))
        self.pushButton_G.setText(_translate("Form", "G"))
        self.pushButton_B.setText(_translate("Form", "B"))
        self.pushButton_C2.setText(_translate("Form", "C"))
        self.pushButton_D2.setText(_translate("Form", "D"))
        self.pushButton_E2.setText(_translate("Form", "E"))
        self.pushButton_F2.setText(_translate("Form", "F"))
        self.pushButton_G2.setText(_translate("Form", "G"))
        self.pushButton_B2.setText(_translate("Form", "B"))
        self.pushButton_C3.setText(_translate("Form", "C"))
        self.pushButton_E3.setText(_translate("Form", "E"))
        self.pushButton_A.setText(_translate("Form", "A"))
        self.pushButton_A2.setText(_translate("Form", "A"))
        self.pushButton_D3.setText(_translate("Form", "D"))
        self.pushButton_Chasz.setText(_translate("Form", "C#"))
        self.pushButton_Dhasz.setText(_translate("Form", "D#"))
        self.pushButton_Fhasz.setText(_translate("Form", "F#"))
        self.pushButton_Ghasz.setText(_translate("Form", "G#"))
        self.pushButton_Ahasz.setText(_translate("Form", "A#"))
        self.pushButton_Chasz2.setText(_translate("Form", "C#"))
        self.pushButton_Dhasz2.setText(_translate("Form", "D#"))
        self.pushButton_Fhasz2.setText(_translate("Form", "F#"))
        self.pushButton_Ghasz2.setText(_translate("Form", "G#"))
        self.pushButton_Ahasz2.setText(_translate("Form", "A#"))
        self.pushButton_Chasz3.setText(_translate("Form", "C#"))
        self.pushButton_Dhasz3.setText(_translate("Form", "D#"))
        self.pushButton_C.setText(_translate("Form", "C"))
        self.labelPianoApp.setText(_translate("Form", "Piano  App"))
        self.label_JakubKielb.setText(_translate("Form", " Jakub Kiełb "))
        self.pushButton.setText(_translate("Form", "t"))
  
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
