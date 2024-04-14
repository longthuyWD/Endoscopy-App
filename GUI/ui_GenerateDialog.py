# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GenerateDialogbVfzad.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_GenerateDialog(object):
    def setupUi(self, GenerateDialog):
        if not GenerateDialog.objectName():
            GenerateDialog.setObjectName(u"GenerateDialog")
        GenerateDialog.resize(480, 299)
        self.verticalLayout_4 = QVBoxLayout(GenerateDialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(GenerateDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fice = QRadioButton(self.frame_2)
        self.fice.setObjectName(u"fice")
        self.fice.setFont(font)

        self.verticalLayout.addWidget(self.fice)

        self.lci = QRadioButton(self.frame_2)
        self.lci.setObjectName(u"lci")
        self.lci.setFont(font)

        self.verticalLayout.addWidget(self.lci)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.albumentation = QRadioButton(self.frame)
        self.albumentation.setObjectName(u"albumentation")
        self.albumentation.setFont(font)

        self.verticalLayout_2.addWidget(self.albumentation)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_3 = QFrame(GenerateDialog)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"QPushButton:pressed{\n"
"	padding-top: 5px;\n"
"}\n"
"\n"
"#btnCancel:hover{\n"
"	border: 2px solid red;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"#btnConfirm:hover{\n"
"	border: 2px solid green;\n"
"	border-radius: 3px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnCancel = QPushButton(self.frame_3)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(100, 40))
        self.btnCancel.setMaximumSize(QSize(100, 40))
        self.btnCancel.setFont(font)

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnConfirm = QPushButton(self.frame_3)
        self.btnConfirm.setObjectName(u"btnConfirm")
        self.btnConfirm.setMinimumSize(QSize(100, 40))
        self.btnConfirm.setMaximumSize(QSize(100, 40))
        self.btnConfirm.setFont(font)

        self.horizontalLayout_2.addWidget(self.btnConfirm)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.retranslateUi(GenerateDialog)

        QMetaObject.connectSlotsByName(GenerateDialog)
    # setupUi

    def retranslateUi(self, GenerateDialog):
        GenerateDialog.setWindowTitle(QCoreApplication.translate("GenerateDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("GenerateDialog", u"Cycle GAN", None))
        self.fice.setText(QCoreApplication.translate("GenerateDialog", u"FICE", None))
        self.lci.setText(QCoreApplication.translate("GenerateDialog", u"LCI", None))
        self.albumentation.setText(QCoreApplication.translate("GenerateDialog", u"Albumentation", None))
        self.btnCancel.setText(QCoreApplication.translate("GenerateDialog", u"Cancel", None))
        self.btnConfirm.setText(QCoreApplication.translate("GenerateDialog", u"Confirm", None))
    # retranslateUi

