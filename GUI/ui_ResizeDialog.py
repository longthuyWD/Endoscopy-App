# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ResizeDialogIlgCzL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ResizeDialog(object):
    def setupUi(self, ResizeDialog):
        if not ResizeDialog.objectName():
            ResizeDialog.setObjectName(u"ResizeDialog")
        ResizeDialog.resize(459, 288)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ResizeDialog.sizePolicy().hasHeightForWidth())
        ResizeDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(ResizeDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(ResizeDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.custom = QRadioButton(self.frame)
        self.custom.setObjectName(u"custom")
        font = QFont()
        font.setPointSize(10)
        self.custom.setFont(font)
        self.custom.setChecked(True)

        self.gridLayout.addWidget(self.custom, 0, 0, 1, 1)

        self.aspect = QRadioButton(self.frame)
        self.aspect.setObjectName(u"aspect")
        self.aspect.setFont(font)

        self.gridLayout.addWidget(self.aspect, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.width = QLineEdit(self.frame_3)
        self.width.setObjectName(u"width")
        self.width.setFont(font)

        self.verticalLayout_2.addWidget(self.width)


        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
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


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(ResizeDialog)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)

        self.resolution = QComboBox(self.frame_2)
        self.resolution.addItem("")
        self.resolution.addItem("")
        self.resolution.addItem("")
        self.resolution.addItem("")
        self.resolution.addItem("")
        self.resolution.setObjectName(u"resolution")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.resolution.sizePolicy().hasHeightForWidth())
        self.resolution.setSizePolicy(sizePolicy2)
        self.resolution.setFont(font)

        self.horizontalLayout.addWidget(self.resolution)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_5 = QFrame(ResizeDialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QPushButton:pressed{\n"
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
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnCancel = QPushButton(self.frame_5)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(100, 40))
        self.btnCancel.setMaximumSize(QSize(100, 40))
        self.btnCancel.setFont(font)

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnConfirm = QPushButton(self.frame_5)
        self.btnConfirm.setObjectName(u"btnConfirm")
        self.btnConfirm.setMinimumSize(QSize(100, 40))
        self.btnConfirm.setMaximumSize(QSize(100, 40))
        self.btnConfirm.setFont(font)

        self.horizontalLayout_2.addWidget(self.btnConfirm)


        self.verticalLayout.addWidget(self.frame_5)


        self.retranslateUi(ResizeDialog)

        QMetaObject.connectSlotsByName(ResizeDialog)
    # setupUi

    def retranslateUi(self, ResizeDialog):
        ResizeDialog.setWindowTitle(QCoreApplication.translate("ResizeDialog", u"Dialog", None))
        self.custom.setText(QCoreApplication.translate("ResizeDialog", u"Custom", None))
        self.aspect.setText(QCoreApplication.translate("ResizeDialog", u"Aspect Ratio", None))
        self.label.setText(QCoreApplication.translate("ResizeDialog", u"Width", None))
        self.label_2.setText(QCoreApplication.translate("ResizeDialog", u"Height", None))
        self.label_3.setText(QCoreApplication.translate("ResizeDialog", u"Resolution", None))
        self.resolution.setItemText(0, QCoreApplication.translate("ResizeDialog", u"Choose...", None))
        self.resolution.setItemText(1, QCoreApplication.translate("ResizeDialog", u"Standard", None))
        self.resolution.setItemText(2, QCoreApplication.translate("ResizeDialog", u"VGA", None))
        self.resolution.setItemText(3, QCoreApplication.translate("ResizeDialog", u"HD", None))
        self.resolution.setItemText(4, QCoreApplication.translate("ResizeDialog", u"Full HD", None))

        self.resolution.setCurrentText(QCoreApplication.translate("ResizeDialog", u"Choose...", None))
        self.btnCancel.setText(QCoreApplication.translate("ResizeDialog", u"Cancel", None))
        self.btnConfirm.setText(QCoreApplication.translate("ResizeDialog", u"Confirm", None))
    # retranslateUi

