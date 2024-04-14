# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CutDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CutDialog(object):
    def setupUi(self, CutDialog):
        if not CutDialog.objectName():
            CutDialog.setObjectName(u"CutDialog")
        CutDialog.resize(447, 345)
        self.verticalLayout = QVBoxLayout(CutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(CutDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.width = QLineEdit(self.frame_3)
        self.width.setObjectName(u"width")
        self.width.setFont(font)

        self.verticalLayout_2.addWidget(self.width)


        self.gridLayout.addWidget(self.frame_3, 2, 0, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2)

        self.height = QLineEdit(self.frame_4)
        self.height.setObjectName(u"height")
        self.height.setFont(font)

        self.verticalLayout_3.addWidget(self.height)


        self.gridLayout.addWidget(self.frame_4, 2, 1, 1, 1)

        self.aspect = QRadioButton(self.frame)
        self.aspect.setObjectName(u"aspect")
        self.aspect.setFont(font)

        self.gridLayout.addWidget(self.aspect, 0, 1, 1, 1)

        self.custom = QRadioButton(self.frame)
        self.custom.setObjectName(u"custom")
        self.custom.setFont(font)
        self.custom.setChecked(True)

        self.gridLayout.addWidget(self.custom, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_6.addWidget(self.label_5)

        self.startX = QLineEdit(self.frame_5)
        self.startX.setObjectName(u"startX")
        self.startX.setFont(font)

        self.verticalLayout_6.addWidget(self.startX)


        self.gridLayout.addWidget(self.frame_5, 1, 0, 1, 1)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_7.addWidget(self.label_6)

        self.startY = QLineEdit(self.frame_6)
        self.startY.setObjectName(u"startY")
        self.startY.setFont(font)

        self.verticalLayout_7.addWidget(self.startY)


        self.gridLayout.addWidget(self.frame_6, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(CutDialog)
        self.frame_2.setObjectName(u"frame_2")
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
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnCancel = QPushButton(self.frame_2)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(100, 40))
        self.btnCancel.setMaximumSize(QSize(100, 40))
        self.btnCancel.setFont(font)
        self.btnCancel.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnConfirm = QPushButton(self.frame_2)
        self.btnConfirm.setObjectName(u"btnConfirm")
        self.btnConfirm.setMinimumSize(QSize(100, 40))
        self.btnConfirm.setMaximumSize(QSize(100, 40))
        self.btnConfirm.setFont(font)
        self.btnConfirm.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btnConfirm)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(CutDialog)

        QMetaObject.connectSlotsByName(CutDialog)
    # setupUi

    def retranslateUi(self, CutDialog):
        CutDialog.setWindowTitle(QCoreApplication.translate("CutDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("CutDialog", u"Right", None))
        self.label_2.setText(QCoreApplication.translate("CutDialog", u"Bottom", None))
        self.aspect.setText(QCoreApplication.translate("CutDialog", u"Aspect Ratio", None))
        self.custom.setText(QCoreApplication.translate("CutDialog", u"Custom", None))
        self.label_5.setText(QCoreApplication.translate("CutDialog", u"Left", None))
        self.startX.setPlaceholderText(QCoreApplication.translate("CutDialog", u"0", None))
        self.label_6.setText(QCoreApplication.translate("CutDialog", u"Top", None))
        self.startY.setPlaceholderText(QCoreApplication.translate("CutDialog", u"0", None))
        self.btnCancel.setText(QCoreApplication.translate("CutDialog", u"Cancel", None))
        self.btnConfirm.setText(QCoreApplication.translate("CutDialog", u"Confirm", None))
    # retranslateUi

