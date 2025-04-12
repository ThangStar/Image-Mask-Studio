# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolbarLayout = QHBoxLayout()
        self.toolbarLayout.setObjectName(u"toolbarLayout")
        self.btnOpen = QPushButton(Form)
        self.btnOpen.setObjectName(u"btnOpen")

        self.toolbarLayout.addWidget(self.btnOpen)

        self.btnSave = QPushButton(Form)
        self.btnSave.setObjectName(u"btnSave")

        self.toolbarLayout.addWidget(self.btnSave)

        self.btnGrid = QPushButton(Form)
        self.btnGrid.setObjectName(u"btnGrid")

        self.toolbarLayout.addWidget(self.btnGrid)

        self.chkDisableAutoEndRow = QCheckBox(Form)
        self.chkDisableAutoEndRow.setObjectName(u"chkDisableAutoEndRow")

        self.toolbarLayout.addWidget(self.chkDisableAutoEndRow)

        self.btnAutoMode = QPushButton(Form)
        self.btnAutoMode.setObjectName(u"btnAutoMode")

        self.toolbarLayout.addWidget(self.btnAutoMode)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.toolbarLayout.addItem(self.horizontalSpacer)

        self.btnTheme = QPushButton(Form)
        self.btnTheme.setObjectName(u"btnTheme")

        self.toolbarLayout.addWidget(self.btnTheme)


        self.verticalLayout.addLayout(self.toolbarLayout)

        self.prg_bar = QProgressBar(Form)
        self.prg_bar.setObjectName(u"prg_bar")
        self.prg_bar.setMinimum(0)
        self.prg_bar.setMaximum(0)

        self.verticalLayout.addWidget(self.prg_bar)

        self.infoWidget = QWidget(Form)
        self.infoWidget.setObjectName(u"infoWidget")
        self.infoWidget.setMaximumSize(QSize(999, 200))
        self.infoLayout = QVBoxLayout(self.infoWidget)
        self.infoLayout.setSpacing(3)
        self.infoLayout.setObjectName(u"infoLayout")
        self.infoLayout.setContentsMargins(0, 3, 0, 3)
        self.lblProcessing = QLabel(self.infoWidget)
        self.lblProcessing.setObjectName(u"lblProcessing")
        self.lblProcessing.setVisible(False)

        self.infoLayout.addWidget(self.lblProcessing)

        self.progressBar = QProgressBar(self.infoWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setVisible(False)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)

        self.infoLayout.addWidget(self.progressBar)

        self.lblGridInfo = QLabel(self.infoWidget)
        self.lblGridInfo.setObjectName(u"lblGridInfo")
        self.lblGridInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.infoLayout.addWidget(self.lblGridInfo)

        self.lblObjectParams = QLabel(self.infoWidget)
        self.lblObjectParams.setObjectName(u"lblObjectParams")
        self.lblObjectParams.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.infoLayout.addWidget(self.lblObjectParams)


        self.verticalLayout.addWidget(self.infoWidget)

        self.imageLabel = QLabel(Form)
        self.imageLabel.setObjectName(u"imageLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.imageLabel)

        self.toolsFrame = QFrame(Form)
        self.toolsFrame.setObjectName(u"toolsFrame")
        self.toolsLayout = QHBoxLayout(self.toolsFrame)
        self.toolsLayout.setObjectName(u"toolsLayout")
        self.btnRotate = QPushButton(self.toolsFrame)
        self.btnRotate.setObjectName(u"btnRotate")

        self.toolsLayout.addWidget(self.btnRotate)

        self.btnFlip = QPushButton(self.toolsFrame)
        self.btnFlip.setObjectName(u"btnFlip")

        self.toolsLayout.addWidget(self.btnFlip)

        self.btnCrop = QPushButton(self.toolsFrame)
        self.btnCrop.setObjectName(u"btnCrop")

        self.toolsLayout.addWidget(self.btnCrop)

        self.btnUpdateAtPos = QPushButton(self.toolsFrame)
        self.btnUpdateAtPos.setObjectName(u"btnUpdateAtPos")

        self.toolsLayout.addWidget(self.btnUpdateAtPos)


        self.verticalLayout.addWidget(self.toolsFrame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Image Processing Studio", None))
        self.btnOpen.setStyleSheet(QCoreApplication.translate("Form", u"QPushButton { \n"
"          background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                  stop:0 #373B44, stop:1 #4286f4);\n"
"          color: white;\n"
"          border: none;\n"
"          padding: 8px 16px;\n"
"          border-radius: 4px;\n"
"          font-weight: bold;\n"
"          letter-spacing: 0.5px;\n"
"        }\n"
"        QPushButton:hover { \n"
"          background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                  stop:0 #434750, stop:1 #5494FF);\n"
"        }\n"
"        QPushButton:pressed {\n"
"          background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                  stop:0 #2B2E35, stop:1 #3573D9);\n"
"        }", None))
        self.btnOpen.setText(QCoreApplication.translate("Form", u"Open Image", None))
        self.btnSave.setStyleSheet(QCoreApplication.translate("Form", u"QPushButton { \n"
"          background-color: transparent; \n"
"          color: #0d6efd; \n"
"          border: 2px solid #0d6efd; \n"
"          padding: 8px 16px; \n"
"          border-radius: 4px; \n"
"        }\n"
"        QPushButton:hover { \n"
"          background-color: #0d6efd; \n"
"          color: white; \n"
"        }", None))
        self.btnSave.setText(QCoreApplication.translate("Form", u"Save", None))
        self.btnGrid.setStyleSheet(QCoreApplication.translate("Form", u"QPushButton { \n"
"          background-color: #198754; \n"
"          color: white; \n"
"          border: none; \n"
"          padding: 8px 16px; \n"
"          border-radius: 4px; \n"
"        }\n"
"        QPushButton:hover { \n"
"          background-color: #157347; \n"
"        }", None))
        self.btnGrid.setText(QCoreApplication.translate("Form", u"Show Grid", None))
        self.chkDisableAutoEndRow.setStyleSheet(QCoreApplication.translate("Form", u"QCheckBox {\n"
"          color: #198754;\n"
"          padding: 8px;\n"
"          font-weight: bold;\n"
"        }\n"
"        QCheckBox::indicator {\n"
"          width: 18px;\n"
"          height: 18px;\n"
"        }\n"
"        QCheckBox::indicator:unchecked {\n"
"          border: 2px solid #198754;\n"
"          border-radius: 3px;\n"
"        }\n"
"        QCheckBox::indicator:checked {\n"
"          background-color: #198754;\n"
"          border: 2px solid #198754;\n"
"          border-radius: 3px;\n"
"        }", None))
        self.chkDisableAutoEndRow.setText(QCoreApplication.translate("Form", u"Disable auto end row", None))
        self.btnAutoMode.setStyleSheet(QCoreApplication.translate("Form", u"QPushButton { \n"
"          background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                    stop:0 #FF6B6B, stop:1 #4ECDC4);\n"
"          color: white;\n"
"          border: none;\n"
"          padding: 8px 16px;\n"
"          border-radius: 4px;\n"
"          font-weight: bold;\n"
"          text-transform: uppercase;\n"
"          letter-spacing: 1px;\n"
"          box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);\n"
"        }\n"
"        QPushButton:hover { \n"
"          background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                    stop:0 #FF8787, stop:1 #6BE5D8);\n"
"          transform: translateY(-2px);\n"
"        }\n"
"        QPushButton:pressed {\n"
"          background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                    stop:0 #E35959, stop:1 #45B8B0);\n"
"        }", None))
        self.btnAutoMode.setText(QCoreApplication.translate("Form", u"Auto Mode", None))
        self.btnTheme.setStyleSheet(QCoreApplication.translate("Form", u"QPushButton { \n"
"          background-color: transparent; \n"
"          color: #198754; \n"
"          border: 2px solid #198754; \n"
"          padding: 8px 16px; \n"
"          border-radius: 4px; \n"
"        }\n"
"        QPushButton:hover { \n"
"          background-color: #198754; \n"
"          color: white; \n"
"        }", None))
        self.btnTheme.setText(QCoreApplication.translate("Form", u"Toggle Theme", None))
        self.prg_bar.setStyleSheet(QCoreApplication.translate("Form", u"QProgressBar {\n"
"        border: 2px solid #0d6efd;\n"
"        border-radius: 5px;\n"
"        text-align: center;\n"
"        height: 25px;\n"
"      }\n"
"      QProgressBar::chunk {\n"
"        background-color: #0d6efd;\n"
"      }", None))
        self.lblProcessing.setStyleSheet(QCoreApplication.translate("Form", u"QLabel { \n"
"           color: #0d6efd;\n"
"           padding: 8px;\n"
"           font-weight: bold;\n"
"           font-family: monospace;\n"
"         }", None))
        self.lblProcessing.setText(QCoreApplication.translate("Form", u"Processing...", None))
        self.progressBar.setStyleSheet(QCoreApplication.translate("Form", u"QProgressBar {\n"
"           border: 2px solid #0d6efd;\n"
"           border-radius: 5px;\n"
"           text-align: center;\n"
"           height: 25px;\n"
"         }\n"
"         QProgressBar::chunk {\n"
"           background-color: #0d6efd;\n"
"         }", None))
        self.lblGridInfo.setStyleSheet(QCoreApplication.translate("Form", u"QLabel { \n"
"           background-color: rgba(255, 255, 255, 200);\n"
"           padding: 8px;\n"
"           border-radius: 4px;\n"
"           font-family: monospace;\n"
"         }", None))
        self.lblGridInfo.setText(QCoreApplication.translate("Form", u"Grid Parameters", None))
        self.lblObjectParams.setStyleSheet(QCoreApplication.translate("Form", u"QLabel { \n"
"           background-color: rgba(255, 255, 255, 200);\n"
"           padding: 8px;\n"
"           border-radius: 4px;\n"
"           font-family: monospace;\n"
"         }", None))
        self.lblObjectParams.setText(QCoreApplication.translate("Form", u"Object Params", None))
        self.imageLabel.setStyleSheet(QCoreApplication.translate("Form", u"border: 1px solid #ccc;", None))
        self.imageLabel.setText(QCoreApplication.translate("Form", u"Drop Image Here", None))
        self.btnRotate.setStyleSheet(QCoreApplication.translate("Form", u"QPushButton { \n"
"          background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                  stop:0 #373B44, stop:1 #4286f4);\n"
"          color: white;\n"
"          border: none;\n"
"          padding: 8px 16px;\n"
"          border-radius: 4px;\n"
"          font-weight: bold;\n"
"          letter-spacing: 0.5px;\n"
"        }\n"
"        QPushButton:hover { \n"
"          background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                  stop:0 #434750, stop:1 #5494FF);\n"
"        }\n"
"        QPushButton:pressed {\n"
"          background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                  stop:0 #2B2E35, stop:1 #3573D9);\n"
"        }", None))
        self.btnRotate.setText(QCoreApplication.translate("Form", u"Rotate", None))
        self.btnFlip.setStyleSheet(QCoreApplication.translate("Form", u"QPushButton { \n"
"          background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                  stop:0 #373B44, stop:1 #4286f4);\n"
"          color: white;\n"
"          border: none;\n"
"          padding: 8px 16px;\n"
"          border-radius: 4px;\n"
"          font-weight: bold;\n"
"          letter-spacing: 0.5px;\n"
"        }\n"
"        QPushButton:hover { \n"
"          background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                  stop:0 #434750, stop:1 #5494FF);\n"
"        }\n"
"        QPushButton:pressed {\n"
"          background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                  stop:0 #2B2E35, stop:1 #3573D9);\n"
"        }", None))
        self.btnFlip.setText(QCoreApplication.translate("Form", u"Flip", None))
        self.btnCrop.setStyleSheet(QCoreApplication.translate("Form", u"QPushButton { \n"
"           background-color: transparent; \n"
"           color: #0d6efd; \n"
"           border: 2px solid #0d6efd; \n"
"           padding: 8px 16px; \n"
"           border-radius: 4px; \n"
"         }\n"
"         QPushButton:hover { \n"
"           background-color: #0d6efd; \n"
"           color: white; \n"
"         }", None))
        self.btnCrop.setText(QCoreApplication.translate("Form", u"Crop", None))
        self.btnUpdateAtPos.setStyleSheet(QCoreApplication.translate("Form", u"QPushButton { \n"
"           background-color: transparent; \n"
"           color: #0d6efd; \n"
"           border: 2px solid #0d6efd; \n"
"           padding: 8px 16px; \n"
"           border-radius: 4px; \n"
"         }\n"
"         QPushButton:hover { \n"
"           background-color: #0d6efd; \n"
"           color: white; \n"
"         }", None))
        self.btnUpdateAtPos.setText(QCoreApplication.translate("Form", u"Update At Pos", None))
    # retranslateUi

