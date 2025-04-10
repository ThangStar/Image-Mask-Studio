# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preview_image.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_PreviewDialog(object):
    def setupUi(self, PreviewDialog):
        if not PreviewDialog.objectName():
            PreviewDialog.setObjectName(u"PreviewDialog")
        PreviewDialog.resize(600, 500)
        self.verticalLayout = QVBoxLayout(PreviewDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.previewLabel = QLabel(PreviewDialog)
        self.previewLabel.setObjectName(u"previewLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previewLabel.sizePolicy().hasHeightForWidth())
        self.previewLabel.setSizePolicy(sizePolicy)
        self.previewLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.previewLabel)

        self.settingsLayout = QHBoxLayout()
        self.settingsLayout.setObjectName(u"settingsLayout")
        self.qualityLabel = QLabel(PreviewDialog)
        self.qualityLabel.setObjectName(u"qualityLabel")

        self.settingsLayout.addWidget(self.qualityLabel)

        self.qualitySpinBox = QSpinBox(PreviewDialog)
        self.qualitySpinBox.setObjectName(u"qualitySpinBox")
        self.qualitySpinBox.setMinimum(1)
        self.qualitySpinBox.setMaximum(100)
        self.qualitySpinBox.setValue(90)

        self.settingsLayout.addWidget(self.qualitySpinBox)

        self.formatLabel = QLabel(PreviewDialog)
        self.formatLabel.setObjectName(u"formatLabel")

        self.settingsLayout.addWidget(self.formatLabel)

        self.formatComboBox = QComboBox(PreviewDialog)
        self.formatComboBox.addItem("")
        self.formatComboBox.addItem("")
        self.formatComboBox.addItem("")
        self.formatComboBox.setObjectName(u"formatComboBox")

        self.settingsLayout.addWidget(self.formatComboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.settingsLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.settingsLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer_2)

        self.btnSave = QPushButton(PreviewDialog)
        self.btnSave.setObjectName(u"btnSave")

        self.buttonLayout.addWidget(self.btnSave)

        self.btnClose = QPushButton(PreviewDialog)
        self.btnClose.setObjectName(u"btnClose")

        self.buttonLayout.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(PreviewDialog)

        QMetaObject.connectSlotsByName(PreviewDialog)
    # setupUi

    def retranslateUi(self, PreviewDialog):
        PreviewDialog.setWindowTitle(QCoreApplication.translate("PreviewDialog", u"Save Image Preview", None))
        self.previewLabel.setStyleSheet(QCoreApplication.translate("PreviewDialog", u"border: 1px solid #ccc;", None))
        self.previewLabel.setText(QCoreApplication.translate("PreviewDialog", u"Image Preview", None))
        self.qualityLabel.setText(QCoreApplication.translate("PreviewDialog", u"Quality:", None))
        self.formatLabel.setText(QCoreApplication.translate("PreviewDialog", u"Format:", None))
        self.formatComboBox.setItemText(0, QCoreApplication.translate("PreviewDialog", u"PNG", None))
        self.formatComboBox.setItemText(1, QCoreApplication.translate("PreviewDialog", u"JPG", None))
        self.formatComboBox.setItemText(2, QCoreApplication.translate("PreviewDialog", u"BMP", None))

        self.btnSave.setStyleSheet(QCoreApplication.translate("PreviewDialog", u"QPushButton { \n"
"          background-color: #0d6efd; \n"
"          color: white; \n"
"          border: none; \n"
"          padding: 8px 16px; \n"
"          border-radius: 4px; \n"
"        }\n"
"        QPushButton:hover { \n"
"          background-color: #0b5ed7; \n"
"        }", None))
        self.btnSave.setText(QCoreApplication.translate("PreviewDialog", u"Save", None))
        self.btnClose.setStyleSheet(QCoreApplication.translate("PreviewDialog", u"QPushButton { \n"
"          background-color: transparent; \n"
"          color: #dc3545; \n"
"          border: 2px solid #dc3545; \n"
"          padding: 8px 16px; \n"
"          border-radius: 4px; \n"
"        }\n"
"        QPushButton:hover { \n"
"          background-color: #dc3545; \n"
"          color: white; \n"
"        }", None))
        self.btnClose.setText(QCoreApplication.translate("PreviewDialog", u"Close", None))
    # retranslateUi

