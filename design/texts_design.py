# Form implementation generated from reading ui file 'Texts_1.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Texts(object):
    def setupUi(self, Texts):
        Texts.setObjectName("Texts")
        Texts.resize(560, 450)
        Texts.setMinimumSize(QtCore.QSize(560, 450))
        Texts.setMaximumSize(QtCore.QSize(560, 450))
        self.choice_title = QtWidgets.QComboBox(Texts)
        self.choice_title.setGeometry(QtCore.QRect(10, 50, 540, 30))
        self.choice_title.setObjectName("choice_title")
        self.result_title = QtWidgets.QLabel(Texts)
        self.result_title.setGeometry(QtCore.QRect(10, 10, 541, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.result_title.setFont(font)
        self.result_title.setObjectName("result_title")
        self.selected_text = QtWidgets.QTextEdit(Texts)
        self.selected_text.setGeometry(QtCore.QRect(10, 90, 540, 350))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.selected_text.setFont(font)
        self.selected_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 4px solid #7b8691;")
        self.selected_text.setReadOnly(True)
        self.selected_text.setObjectName("selected_text")

        self.retranslateUi(Texts)
        QtCore.QMetaObject.connectSlotsByName(Texts)

    def retranslateUi(self, Texts):
        _translate = QtCore.QCoreApplication.translate
        Texts.setWindowTitle(_translate("Texts", "Тексты"))
        self.result_title.setText(_translate("Texts", "Выбор названия статьи:"))
        self.selected_text.setHtml(_translate("Texts", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
