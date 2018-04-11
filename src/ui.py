# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(955, 656)
        self.pic_label = QtWidgets.QLabel(Dialog)
        self.pic_label.setGeometry(QtCore.QRect(50, 40, 861, 501))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pic_label.sizePolicy().hasHeightForWidth())
        self.pic_label.setSizePolicy(sizePolicy)
        self.pic_label.setText("")
        self.pic_label.setScaledContents(True)
        self.pic_label.setObjectName("pic_label")
        self.movieName = QtWidgets.QLabel(Dialog)
        self.movieName.setGeometry(QtCore.QRect(160, 580, 621, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.movieName.setFont(font)
        self.movieName.setScaledContents(True)
        self.movieName.setAlignment(QtCore.Qt.AlignCenter)
        self.movieName.setObjectName("movieName")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.movieName.setText(_translate("Dialog", "TextLabel"))

