# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(890, 574)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 851, 471))
        self.tab_config = QWidget()
        self.tab_config.setObjectName(u"tab_config")
        self.tab_config.setEnabled(True)
        self.verticalLayoutWidget = QWidget(self.tab_config)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 811, 441))
        self.verticalLayout_ofTabConfig = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_ofTabConfig.setSpacing(0)
        self.verticalLayout_ofTabConfig.setObjectName(u"verticalLayout_ofTabConfig")
        self.verticalLayout_ofTabConfig.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_ofTabConfig.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        self.formLayoutWidget = QWidget(self.groupBox_2)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 371, 211))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(50)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.doubleSpinBox_timeout = QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_timeout.setObjectName(u"doubleSpinBox_timeout")
        self.doubleSpinBox_timeout.setDecimals(1)
        self.doubleSpinBox_timeout.setValue(5.000000000000000)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_timeout)

        self.doubleSpinBox_buffer = QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_buffer.setObjectName(u"doubleSpinBox_buffer")
        self.doubleSpinBox_buffer.setDecimals(1)
        self.doubleSpinBox_buffer.setValue(0.100000000000000)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_buffer)

        self.doubleSpinBox_throttle = QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_throttle.setObjectName(u"doubleSpinBox_throttle")
        self.doubleSpinBox_throttle.setDecimals(1)
        self.doubleSpinBox_throttle.setValue(0.100000000000000)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_throttle)

        self.doubleSpinBox_heartbeat = QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_heartbeat.setObjectName(u"doubleSpinBox_heartbeat")
        self.doubleSpinBox_heartbeat.setDecimals(1)
        self.doubleSpinBox_heartbeat.setValue(30.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_heartbeat)

        self.lineEdit_uri = QLineEdit(self.formLayoutWidget)
        self.lineEdit_uri.setObjectName(u"lineEdit_uri")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_uri)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayoutWidget_2 = QWidget(self.groupBox)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 20, 371, 211))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(50)
        self.formLayout_2.setVerticalSpacing(6)
        self.formLayout_2.setContentsMargins(10, 0, 0, 0)
        self.label_6 = QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.label_7 = QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.label_8 = QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.label_9 = QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.label_10 = QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.label_11 = QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.label_12 = QLabel(self.formLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_12)

        self.label_13 = QLabel(self.formLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_13)

        self.label_14 = QLabel(self.formLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_14)

        self.checkBox_provider = QCheckBox(self.formLayoutWidget_2)
        self.checkBox_provider.setObjectName(u"checkBox_provider")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.checkBox_provider)

        self.checkBox_player = QCheckBox(self.formLayoutWidget_2)
        self.checkBox_player.setObjectName(u"checkBox_player")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.checkBox_player)

        self.checkBox_hero = QCheckBox(self.formLayoutWidget_2)
        self.checkBox_hero.setObjectName(u"checkBox_hero")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.checkBox_hero)

        self.checkBox_map = QCheckBox(self.formLayoutWidget_2)
        self.checkBox_map.setObjectName(u"checkBox_map")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.checkBox_map)

        self.checkBox_buildings = QCheckBox(self.formLayoutWidget_2)
        self.checkBox_buildings.setObjectName(u"checkBox_buildings")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.checkBox_buildings)

        self.checkBox_abilities = QCheckBox(self.formLayoutWidget_2)
        self.checkBox_abilities.setObjectName(u"checkBox_abilities")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.FieldRole, self.checkBox_abilities)

        self.checkBox_items = QCheckBox(self.formLayoutWidget_2)
        self.checkBox_items.setObjectName(u"checkBox_items")

        self.formLayout_2.setWidget(6, QFormLayout.ItemRole.FieldRole, self.checkBox_items)

        self.checkBox_draft = QCheckBox(self.formLayoutWidget_2)
        self.checkBox_draft.setObjectName(u"checkBox_draft")

        self.formLayout_2.setWidget(7, QFormLayout.ItemRole.FieldRole, self.checkBox_draft)

        self.checkBox_wearables = QCheckBox(self.formLayoutWidget_2)
        self.checkBox_wearables.setObjectName(u"checkBox_wearables")

        self.formLayout_2.setWidget(8, QFormLayout.ItemRole.FieldRole, self.checkBox_wearables)


        self.horizontalLayout.addWidget(self.groupBox)


        self.verticalLayout_ofTabConfig.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(16)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.pushButton_updateConfigGSI = QPushButton(self.verticalLayoutWidget)
        self.pushButton_updateConfigGSI.setObjectName(u"pushButton_updateConfigGSI")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_updateConfigGSI.sizePolicy().hasHeightForWidth())
        self.pushButton_updateConfigGSI.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.pushButton_updateConfigGSI)

        self.label_17 = QLabel(self.verticalLayoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_2.addWidget(self.label_17)

        self.label_updateConfigStatus = QLabel(self.verticalLayoutWidget)
        self.label_updateConfigStatus.setObjectName(u"label_updateConfigStatus")

        self.horizontalLayout_2.addWidget(self.label_updateConfigStatus)

        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 10)

        self.verticalLayout_ofTabConfig.addLayout(self.horizontalLayout_2)

        self.verticalLayout_ofTabConfig.setStretch(0, 5)
        self.verticalLayout_ofTabConfig.setStretch(1, 1)
        self.tabWidget.addTab(self.tab_config, "")
        self.tab_info = QWidget()
        self.tab_info.setObjectName(u"tab_info")
        self.verticalLayoutWidget_2 = QWidget(self.tab_info)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 0, 821, 431))
        self.verticalLayout_ofTabInfo = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_ofTabInfo.setSpacing(0)
        self.verticalLayout_ofTabInfo.setObjectName(u"verticalLayout_ofTabInfo")
        self.verticalLayout_ofTabInfo.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 1, -1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_runServer = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_runServer.setObjectName(u"pushButton_runServer")
        sizePolicy.setHeightForWidth(self.pushButton_runServer.sizePolicy().hasHeightForWidth())
        self.pushButton_runServer.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.pushButton_runServer)

        self.label_15 = QLabel(self.verticalLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_5.addWidget(self.label_15)

        self.label_serverStatus = QLabel(self.verticalLayoutWidget_2)
        self.label_serverStatus.setObjectName(u"label_serverStatus")

        self.horizontalLayout_5.addWidget(self.label_serverStatus)

        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(1, 2)
        self.horizontalLayout_5.setStretch(2, 10)

        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_ofTabInfo.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.textBrowser = QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_4.addWidget(self.textBrowser)


        self.verticalLayout_ofTabInfo.addLayout(self.horizontalLayout_4)

        self.verticalLayout_ofTabInfo.setStretch(0, 1)
        self.verticalLayout_ofTabInfo.setStretch(1, 7)
        self.tabWidget.addTab(self.tab_info, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Dota GSI", None))
#if QT_CONFIG(accessibility)
        self.tabWidget.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"ConfigGSI", None))
        self.label.setText(QCoreApplication.translate("Form", u"uri", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"timeout", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"buffer", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"throttle", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"heartbeat", None))
        self.lineEdit_uri.setText(QCoreApplication.translate("Form", u"http://localhost:8070/", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"ConfigGSIData (Select data to recive)", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"provider", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"player", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"hero", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"map", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"buildings", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"abilities", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"wearables", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"draft", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"items", None))
        self.checkBox_provider.setText("")
        self.checkBox_player.setText("")
        self.checkBox_hero.setText("")
        self.checkBox_map.setText("")
        self.checkBox_buildings.setText("")
        self.checkBox_abilities.setText("")
        self.checkBox_items.setText("")
        self.checkBox_draft.setText("")
        self.checkBox_wearables.setText("")
        self.pushButton_updateConfigGSI.setText(QCoreApplication.translate("Form", u"Update ConfigGSI", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Status:", None))
        self.label_updateConfigStatus.setText(QCoreApplication.translate("Form", u"1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_config), QCoreApplication.translate("Form", u"Config", None))
        self.pushButton_runServer.setText(QCoreApplication.translate("Form", u"Run server", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Server Status: ", None))
        self.label_serverStatus.setText(QCoreApplication.translate("Form", u"OFF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_info), QCoreApplication.translate("Form", u"Info", None))
    # retranslateUi

