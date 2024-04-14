# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CleannessDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CleannessDialog(object):
    def setupUi(self, CleannessDialog):
        if not CleannessDialog.objectName():
            CleannessDialog.setObjectName(u"CleannessDialog")
        CleannessDialog.resize(400, 256)
        self.verticalLayout = QVBoxLayout(CleannessDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(CleannessDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.threshold = QLineEdit(self.frame)
        self.threshold.setObjectName(u"threshold")
        self.threshold.setFont(font)
        self.threshold.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.threshold)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(CleannessDialog)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"QPushButton:pressed{\n"
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
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnCancel = QPushButton(self.frame_2)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(100, 40))
        self.btnCancel.setMaximumSize(QSize(100, 40))
        self.btnCancel.setFont(font)

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnConfirm = QPushButton(self.frame_2)
        self.btnConfirm.setObjectName(u"btnConfirm")
        self.btnConfirm.setMinimumSize(QSize(100, 40))
        self.btnConfirm.setMaximumSize(QSize(100, 40))
        self.btnConfirm.setFont(font)

        self.horizontalLayout_2.addWidget(self.btnConfirm)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(CleannessDialog)

        QMetaObject.connectSlotsByName(CleannessDialog)
    # setupUi

    def retranslateUi(self, CleannessDialog):
        CleannessDialog.setWindowTitle(QCoreApplication.translate("CleannessDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("CleannessDialog", u"Threshold", None))
        self.threshold.setPlaceholderText(QCoreApplication.translate("CleannessDialog", u"0.3", None))
        self.btnCancel.setText(QCoreApplication.translate("CleannessDialog", u"Cancel", None))
        self.btnConfirm.setText(QCoreApplication.translate("CleannessDialog", u"Confirm", None))
    # retranslateUi

