# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 594)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(600, 600))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(10, 0, 10, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QtCore.QSize(600, 600))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.reset_button = QtWidgets.QPushButton(self.frame_3)
        self.reset_button.setObjectName("reset_button")
        self.gridLayout_25.addWidget(self.reset_button, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.gridLayout_8.addWidget(self.frame_3, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.frame_4)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_3.addWidget(self.frame_10, 0, 0, 1, 1)
        self.frame_13 = QtWidgets.QFrame(self.frame_4)
        self.frame_13.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_13.setSizeIncrement(QtCore.QSize(0, 50))
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.pushButton_39 = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_39.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_39.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_39.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_39.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_39.setText("")
        self.pushButton_39.setObjectName("pushButton_39")
        self.gridLayout_9.addWidget(self.pushButton_39, 0, 0, 1, 1)
        self.pushButton_38 = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_38.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_38.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_38.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_38.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_38.setText("")
        self.pushButton_38.setObjectName("pushButton_38")
        self.gridLayout_9.addWidget(self.pushButton_38, 0, 1, 1, 1)
        self.pushButton_37 = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_37.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_37.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_37.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_37.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_37.setText("")
        self.pushButton_37.setObjectName("pushButton_37")
        self.gridLayout_9.addWidget(self.pushButton_37, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.frame_13, 2, 0, 1, 1)
        self.frame_14 = QtWidgets.QFrame(self.frame_4)
        self.frame_14.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_14.setSizeIncrement(QtCore.QSize(0, 50))
        self.frame_14.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_14.setObjectName("frame_14")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_14)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.pushButton_49 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_49.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_49.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_49.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_49.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_49.setText("")
        self.pushButton_49.setObjectName("pushButton_49")
        self.gridLayout_13.addWidget(self.pushButton_49, 0, 0, 1, 1)
        self.pushButton_50 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_50.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_50.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_50.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_50.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_50.setText("")
        self.pushButton_50.setObjectName("pushButton_50")
        self.gridLayout_13.addWidget(self.pushButton_50, 0, 1, 1, 1)
        self.pushButton_51 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_51.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_51.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_51.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_51.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_51.setText("")
        self.pushButton_51.setObjectName("pushButton_51")
        self.gridLayout_13.addWidget(self.pushButton_51, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.frame_14, 1, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_4, 0, 1, 1, 1)
        self.frame_12 = QtWidgets.QFrame(self.frame_2)
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_8.addWidget(self.frame_12, 0, 2, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_16 = QtWidgets.QFrame(self.frame_7)
        self.frame_16.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_16.setSizeIncrement(QtCore.QSize(0, 50))
        self.frame_16.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_16.setObjectName("frame_16")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_16)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.pushButton_55 = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_55.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_55.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_55.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_55.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_55.setText("")
        self.pushButton_55.setObjectName("pushButton_55")
        self.gridLayout_15.addWidget(self.pushButton_55, 0, 0, 1, 1)
        self.pushButton_56 = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_56.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_56.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_56.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_56.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_56.setText("")
        self.pushButton_56.setObjectName("pushButton_56")
        self.gridLayout_15.addWidget(self.pushButton_56, 0, 1, 1, 1)
        self.pushButton_57 = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_57.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_57.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_57.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_57.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_57.setText("")
        self.pushButton_57.setObjectName("pushButton_57")
        self.gridLayout_15.addWidget(self.pushButton_57, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.frame_16, 1, 0, 1, 1)
        self.frame_15 = QtWidgets.QFrame(self.frame_7)
        self.frame_15.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_15.setSizeIncrement(QtCore.QSize(0, 50))
        self.frame_15.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.pushButton_52 = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_52.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_52.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_52.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_52.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_52.setText("")
        self.pushButton_52.setObjectName("pushButton_52")
        self.gridLayout_14.addWidget(self.pushButton_52, 0, 0, 1, 1)
        self.pushButton_53 = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_53.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_53.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_53.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_53.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_53.setText("")
        self.pushButton_53.setObjectName("pushButton_53")
        self.gridLayout_14.addWidget(self.pushButton_53, 0, 1, 1, 1)
        self.pushButton_54 = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_54.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_54.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_54.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_54.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_54.setText("")
        self.pushButton_54.setObjectName("pushButton_54")
        self.gridLayout_14.addWidget(self.pushButton_54, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.frame_15, 0, 0, 1, 1)
        self.frame_17 = QtWidgets.QFrame(self.frame_7)
        self.frame_17.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_17.setSizeIncrement(QtCore.QSize(0, 50))
        self.frame_17.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_17.setObjectName("frame_17")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.frame_17)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.pushButton_58 = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_58.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_58.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_58.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_58.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_58.setText("")
        self.pushButton_58.setObjectName("pushButton_58")
        self.gridLayout_16.addWidget(self.pushButton_58, 0, 0, 1, 1)
        self.pushButton_59 = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_59.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_59.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_59.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_59.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_59.setText("")
        self.pushButton_59.setObjectName("pushButton_59")
        self.gridLayout_16.addWidget(self.pushButton_59, 0, 1, 1, 1)
        self.pushButton_60 = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_60.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_60.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_60.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_60.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_60.setText("")
        self.pushButton_60.setObjectName("pushButton_60")
        self.gridLayout_16.addWidget(self.pushButton_60, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.frame_17, 2, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_7, 1, 1, 1, 1)
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_8.addWidget(self.frame_9, 2, 0, 1, 1)
        self.frame_11 = QtWidgets.QFrame(self.frame_2)
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_8.addWidget(self.frame_11, 2, 2, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_18 = QtWidgets.QFrame(self.frame_5)
        self.frame_18.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_18.setSizeIncrement(QtCore.QSize(0, 50))
        self.frame_18.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.frame_18.setObjectName("frame_18")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.frame_18)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.pushButton_61 = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_61.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_61.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_61.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_61.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_61.setText("")
        self.pushButton_61.setObjectName("pushButton_61")
        self.gridLayout_17.addWidget(self.pushButton_61, 0, 2, 1, 1)
        self.pushButton_62 = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_62.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_62.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_62.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_62.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_62.setText("")
        self.pushButton_62.setObjectName("pushButton_62")
        self.gridLayout_17.addWidget(self.pushButton_62, 0, 0, 1, 1)
        self.pushButton_63 = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_63.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_63.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_63.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_63.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_63.setText("")
        self.pushButton_63.setObjectName("pushButton_63")
        self.gridLayout_17.addWidget(self.pushButton_63, 0, 1, 1, 1)
        self.frame_19 = QtWidgets.QFrame(self.frame_18)
        self.frame_19.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_19.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_19.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_19.setObjectName("frame_19")
        self.gridLayout_17.addWidget(self.frame_19, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_18, 2, 0, 1, 1)
        self.frame_20 = QtWidgets.QFrame(self.frame_5)
        self.frame_20.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_20.setSizeIncrement(QtCore.QSize(0, 50))
        self.frame_20.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_20.setObjectName("frame_20")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.frame_20)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.pushButton_64 = QtWidgets.QPushButton(self.frame_20)
        self.pushButton_64.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_64.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_64.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_64.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_64.setText("")
        self.pushButton_64.setObjectName("pushButton_64")
        self.gridLayout_18.addWidget(self.pushButton_64, 0, 0, 1, 1)
        self.pushButton_65 = QtWidgets.QPushButton(self.frame_20)
        self.pushButton_65.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_65.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_65.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_65.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_65.setText("")
        self.pushButton_65.setObjectName("pushButton_65")
        self.gridLayout_18.addWidget(self.pushButton_65, 0, 1, 1, 1)
        self.pushButton_66 = QtWidgets.QPushButton(self.frame_20)
        self.pushButton_66.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_66.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_66.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_66.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_66.setText("")
        self.pushButton_66.setObjectName("pushButton_66")
        self.gridLayout_18.addWidget(self.pushButton_66, 0, 2, 1, 1)
        self.gridLayout_7.addWidget(self.frame_20, 1, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_5, 2, 1, 1, 1)
        self.frame_21 = QtWidgets.QFrame(self.frame_2)
        self.frame_21.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_21.setObjectName("frame_21")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_21)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_22 = QtWidgets.QFrame(self.frame_21)
        self.frame_22.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_22.setSizeIncrement(QtCore.QSize(0, 50))
        self.frame_22.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_22.setObjectName("frame_22")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.frame_22)
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.pushButton_67 = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_67.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_67.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_67.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_67.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_67.setText("")
        self.pushButton_67.setObjectName("pushButton_67")
        self.gridLayout_19.addWidget(self.pushButton_67, 0, 2, 1, 1)
        self.pushButton_68 = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_68.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_68.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_68.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_68.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_68.setText("")
        self.pushButton_68.setObjectName("pushButton_68")
        self.gridLayout_19.addWidget(self.pushButton_68, 0, 1, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.frame_22)
        self.frame_6.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_6.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_19.addWidget(self.frame_6, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_22, 0, 0, 1, 1)
        self.frame_23 = QtWidgets.QFrame(self.frame_21)
        self.frame_23.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_23.setSizeIncrement(QtCore.QSize(0, 50))
        self.frame_23.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_23.setObjectName("frame_23")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.frame_23)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.pushButton_69 = QtWidgets.QPushButton(self.frame_23)
        self.pushButton_69.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_69.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_69.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_69.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_69.setText("")
        self.pushButton_69.setObjectName("pushButton_69")
        self.gridLayout_20.addWidget(self.pushButton_69, 0, 2, 1, 1)
        self.pushButton_70 = QtWidgets.QPushButton(self.frame_23)
        self.pushButton_70.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_70.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_70.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_70.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_70.setText("")
        self.pushButton_70.setObjectName("pushButton_70")
        self.gridLayout_20.addWidget(self.pushButton_70, 0, 1, 1, 1)
        self.frame_24 = QtWidgets.QFrame(self.frame_23)
        self.frame_24.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_24.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_24.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_24.setObjectName("frame_24")
        self.gridLayout_20.addWidget(self.frame_24, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_23, 2, 0, 1, 1)
        self.frame_25 = QtWidgets.QFrame(self.frame_21)
        self.frame_25.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_25.setSizeIncrement(QtCore.QSize(0, 50))
        self.frame_25.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_25.setObjectName("frame_25")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.frame_25)
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.pushButton_71 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_71.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_71.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_71.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_71.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_71.setText("")
        self.pushButton_71.setObjectName("pushButton_71")
        self.gridLayout_21.addWidget(self.pushButton_71, 0, 2, 1, 1)
        self.pushButton_72 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_72.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_72.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_72.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_72.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_72.setText("")
        self.pushButton_72.setObjectName("pushButton_72")
        self.gridLayout_21.addWidget(self.pushButton_72, 0, 1, 1, 1)
        self.frame_26 = QtWidgets.QFrame(self.frame_25)
        self.frame_26.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_26.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_26.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_26.setObjectName("frame_26")
        self.gridLayout_21.addWidget(self.frame_26, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_25, 1, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_21, 1, 0, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_27 = QtWidgets.QFrame(self.frame_8)
        self.frame_27.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_27.setSizeIncrement(QtCore.QSize(0, 50))
        self.frame_27.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_27.setObjectName("frame_27")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.frame_27)
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.pushButton_73 = QtWidgets.QPushButton(self.frame_27)
        self.pushButton_73.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_73.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_73.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_73.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_73.setText("")
        self.pushButton_73.setObjectName("pushButton_73")
        self.gridLayout_22.addWidget(self.pushButton_73, 0, 1, 1, 1)
        self.pushButton_74 = QtWidgets.QPushButton(self.frame_27)
        self.pushButton_74.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_74.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_74.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_74.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_74.setText("")
        self.pushButton_74.setObjectName("pushButton_74")
        self.gridLayout_22.addWidget(self.pushButton_74, 0, 0, 1, 1)
        self.frame_28 = QtWidgets.QFrame(self.frame_27)
        self.frame_28.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_28.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_28.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_28.setObjectName("frame_28")
        self.gridLayout_22.addWidget(self.frame_28, 0, 2, 1, 1)
        self.gridLayout_6.addWidget(self.frame_27, 1, 0, 1, 1)
        self.frame_29 = QtWidgets.QFrame(self.frame_8)
        self.frame_29.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_29.setSizeIncrement(QtCore.QSize(0, 50))
        self.frame_29.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_29.setObjectName("frame_29")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.frame_29)
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.pushButton_75 = QtWidgets.QPushButton(self.frame_29)
        self.pushButton_75.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_75.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_75.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_75.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_75.setText("")
        self.pushButton_75.setObjectName("pushButton_75")
        self.gridLayout_23.addWidget(self.pushButton_75, 0, 1, 1, 1)
        self.pushButton_76 = QtWidgets.QPushButton(self.frame_29)
        self.pushButton_76.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_76.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_76.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_76.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_76.setText("")
        self.pushButton_76.setObjectName("pushButton_76")
        self.gridLayout_23.addWidget(self.pushButton_76, 0, 0, 1, 1)
        self.frame_30 = QtWidgets.QFrame(self.frame_29)
        self.frame_30.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_30.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_30.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_30.setObjectName("frame_30")
        self.gridLayout_23.addWidget(self.frame_30, 0, 2, 1, 1)
        self.gridLayout_6.addWidget(self.frame_29, 0, 0, 1, 1)
        self.frame_31 = QtWidgets.QFrame(self.frame_8)
        self.frame_31.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_31.setSizeIncrement(QtCore.QSize(0, 50))
        self.frame_31.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_31.setObjectName("frame_31")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.frame_31)
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.pushButton_77 = QtWidgets.QPushButton(self.frame_31)
        self.pushButton_77.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_77.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_77.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_77.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_77.setText("")
        self.pushButton_77.setObjectName("pushButton_77")
        self.gridLayout_24.addWidget(self.pushButton_77, 0, 0, 1, 1)
        self.pushButton_78 = QtWidgets.QPushButton(self.frame_31)
        self.pushButton_78.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_78.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_78.setSizeIncrement(QtCore.QSize(40, 40))
        self.pushButton_78.setStyleSheet("background-color: white;\n"
"border-radius:20px;")
        self.pushButton_78.setText("")
        self.pushButton_78.setObjectName("pushButton_78")
        self.gridLayout_24.addWidget(self.pushButton_78, 0, 1, 1, 1)
        self.frame_32 = QtWidgets.QFrame(self.frame_31)
        self.frame_32.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_32.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_32.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_32.setObjectName("frame_32")
        self.gridLayout_24.addWidget(self.frame_32, 0, 2, 1, 1)
        self.gridLayout_6.addWidget(self.frame_31, 2, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_8, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.reset_button.setText(_translate("MainWindow", "リセット"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())