# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'un.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


# class Ui_Form(object):
#     def setupUi(self, Form):
#         if not Form.objectName():
#             Form.setObjectName(u"Form")
#         Form.resize(631, 586)
#         self.textEdit = QTextEdit(Form)
#         self.textEdit.setObjectName(u"textEdit")
#         self.textEdit.setGeometry(QRect(90, 250, 104, 87))
#         self.lineEdit = QLineEdit(Form)
#         self.lineEdit.setObjectName(u"lineEdit")
#         self.lineEdit.setGeometry(QRect(90, 140, 113, 22))
#         self.spinBox = QSpinBox(Form)
#         self.spinBox.setObjectName(u"spinBox")
#         self.spinBox.setGeometry(QRect(130, 410, 42, 22))
#         self.doubleSpinBox = QDoubleSpinBox(Form)
#         self.doubleSpinBox.setObjectName(u"doubleSpinBox")
#         self.doubleSpinBox.setGeometry(QRect(130, 510, 62, 22))
#         self.dateEdit = QDateEdit(Form)
#         self.dateEdit.setObjectName(u"dateEdit")
#         self.dateEdit.setGeometry(QRect(260, 460, 110, 22))
#         self.dateTimeEdit = QDateTimeEdit(Form)
#         self.dateTimeEdit.setObjectName(u"dateTimeEdit")
#         self.dateTimeEdit.setGeometry(QRect(330, 390, 194, 22))
#         self.dial = QDial(Form)
#         self.dial.setObjectName(u"dial")
#         self.dial.setGeometry(QRect(390, 490, 50, 64))
#         self.comboBox = QComboBox(Form)
#         self.comboBox.setObjectName(u"comboBox")
#         self.comboBox.setGeometry(QRect(310, 170, 73, 22))
#         self.keySequenceEdit = QKeySequenceEdit(Form)
#         self.keySequenceEdit.setObjectName(u"keySequenceEdit")
#         self.keySequenceEdit.setGeometry(QRect(30, 460, 113, 24))

#         self.retranslateUi(Form)

#         QMetaObject.connectSlotsByName(Form)
#     # setupUi

#     def retranslateUi(self, Form):
#         Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#     # retranslateUi


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.label_2 = QLabel()
        layout.addWidget(self.label_2)
        self.line_edit_2 = QLineEdit()
        layout.addWidget(self.line_edit_2)
        self.label_3 = QLabel()
        layout.addWidget(self.label_3)

        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)

        self.label = QLabel()
        layout.addWidget(self.label)
        self.label_4 = QLabel()
        layout.addWidget(self.label_4)

        self.line_edit.textChanged.connect(self.line_edit_text_changed)
        
        self.label_2.setText('Введите ваш вес ниже')
        self.label_3.setText('Введите ваш рост ниже в метрах обязательно')
        self.label_4.setText('Ваш статус: ')
        self.show()

    def line_edit_text_changed(self, text):
        a = self.line_edit_2.displayText()
        try:
            a = float(a)
        except ValueError:
            self.label.setText('Ошибка ввода данных! Пишите рост через точку, а вес целым числом, например: рост - 1.8, вес - 60')
        try:
            text = float(text)
        except ValueError:
            self.label.setText('Ошибка ввода данных! Пишите рост через точку, а вес целым числом, например: рост - 1.8, вес - 60')    
        text = a / text**2 
        text = round(text, 2)
        if text > 40:
            self.label_4.setText('Ваш статус: Ожирение 3 степени!\n Немедленно обратитесь к врачу!!!!!')
        if text > 35 and text < 39.9:
            self.label_4.setText('Ваш статус: Ожирение 2 степени!\n Обратитесь к врачу!!!')
        if text > 30 and text < 34.9:
            self.label_4.setText('Ваш статус: Ожирение 1 степени!\n Обратитесь к врачу и измените образ жизни!')
        if text < 29.9 and text >25:
            self.label_4.setText('Ваш статус: избыточный вес!\n Кому стоит в серьез задуматься о спорте!)')
        if text < 24.9 and text > 18.5:
            self.label_4.setText('Ваш статус: нормальный вес, ура!\n Оставайтесь в том же весе!)')
        if text < 18.5:
            self.label_4.setText('Ваш статус: недостаток веса!\n Надеюсь не очень сильный,\n возможно стоит обратиться к врачу')
        text = str(text)
        self.label.setText('ваш индекс массы тела: ' + text)
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    # Form = QWidget()
    # ui = Ui_Form()
    # ui.setupUi(Form)
    # Form.show()
    mv = MainWindow()
    sys.exit(app.exec_())