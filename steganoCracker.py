# Form implementation generated from reading ui file 'steganoCracker.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_steganoCracker(object):
    def setupUi(self, steganoCracker):
        steganoCracker.setObjectName("steganoCracker")
        steganoCracker.resize(855, 584)
        steganoCracker.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.label_path = QtWidgets.QLabel(parent=steganoCracker)
        self.label_path.setGeometry(QtCore.QRect(11, 11, 400, 16))
        self.label_path.setScaledContents(False)
        self.label_path.setObjectName("label_path")
        self.label_operation = QtWidgets.QLabel(parent=steganoCracker)
        self.label_operation.setGeometry(QtCore.QRect(11, 71, 200, 16))
        self.label_operation.setObjectName("label_operation")
        self.comboBox_operation = QtWidgets.QComboBox(parent=steganoCracker)
        self.comboBox_operation.setGeometry(QtCore.QRect(11, 91, 150, 23))
        self.comboBox_operation.setObjectName("comboBox_operation")
        self.comboBox_operation.addItem("")
        self.comboBox_operation.addItem("")
        self.graphicsView_image = QtWidgets.QGraphicsView(parent=steganoCracker)
        self.graphicsView_image.setGeometry(QtCore.QRect(241, 71, 600, 360))
        self.graphicsView_image.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.graphicsView_image.setObjectName("graphicsView_image")
        self.layoutWidget = QtWidgets.QWidget(parent=steganoCracker)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 32, 831, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_path = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_path.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_path.setObjectName("gridLayout_path")
        self.pushButton_browse = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_browse.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButton_browse.setObjectName("pushButton_browse")
        self.gridLayout_path.addWidget(self.pushButton_browse, 0, 1, 1, 1)
        self.lineEdit_path = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.gridLayout_path.addWidget(self.lineEdit_path, 0, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(parent=steganoCracker)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 150, 110, 77))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_subpixels = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_subpixels.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_subpixels.setObjectName("gridLayout_subpixels")
        self.radioButton_grb = QtWidgets.QRadioButton(parent=self.layoutWidget1)
        self.radioButton_grb.setObjectName("radioButton_grb")
        self.gridLayout_subpixels.addWidget(self.radioButton_grb, 1, 0, 1, 1)
        self.radioButton_rbg = QtWidgets.QRadioButton(parent=self.layoutWidget1)
        self.radioButton_rbg.setObjectName("radioButton_rbg")
        self.gridLayout_subpixels.addWidget(self.radioButton_rbg, 0, 1, 1, 1)
        self.radioButton_brg = QtWidgets.QRadioButton(parent=self.layoutWidget1)
        self.radioButton_brg.setObjectName("radioButton_brg")
        self.gridLayout_subpixels.addWidget(self.radioButton_brg, 2, 0, 1, 1)
        self.radioButton_gbr = QtWidgets.QRadioButton(parent=self.layoutWidget1)
        self.radioButton_gbr.setObjectName("radioButton_gbr")
        self.gridLayout_subpixels.addWidget(self.radioButton_gbr, 1, 1, 1, 1)
        self.radioButton_rgb = QtWidgets.QRadioButton(parent=self.layoutWidget1)
        self.radioButton_rgb.setChecked(True)
        self.radioButton_rgb.setObjectName("radioButton_rgb")
        self.gridLayout_subpixels.addWidget(self.radioButton_rgb, 0, 0, 1, 1)
        self.radioButton_bgr = QtWidgets.QRadioButton(parent=self.layoutWidget1)
        self.radioButton_bgr.setObjectName("radioButton_bgr")
        self.gridLayout_subpixels.addWidget(self.radioButton_bgr, 2, 1, 1, 1)
        self.label_subpixels = QtWidgets.QLabel(parent=steganoCracker)
        self.label_subpixels.setGeometry(QtCore.QRect(11, 131, 200, 16))
        self.label_subpixels.setObjectName("label_subpixels")
        self.label_pattern = QtWidgets.QLabel(parent=steganoCracker)
        self.label_pattern.setGeometry(QtCore.QRect(11, 271, 200, 16))
        self.label_pattern.setObjectName("label_pattern")
        self.comboBox_pattern = QtWidgets.QComboBox(parent=steganoCracker)
        self.comboBox_pattern.setGeometry(QtCore.QRect(11, 291, 150, 23))
        self.comboBox_pattern.setObjectName("comboBox_pattern")
        self.comboBox_pattern.addItem("")
        self.comboBox_pattern.addItem("")
        self.comboBox_pattern.addItem("")
        self.label_order = QtWidgets.QLabel(parent=steganoCracker)
        self.label_order.setGeometry(QtCore.QRect(11, 331, 200, 16))
        self.label_order.setObjectName("label_order")
        self.comboBox_order = QtWidgets.QComboBox(parent=steganoCracker)
        self.comboBox_order.setGeometry(QtCore.QRect(11, 351, 150, 23))
        self.comboBox_order.setObjectName("comboBox_order")
        self.comboBox_order.addItem("")
        self.comboBox_order.addItem("")
        self.label_number = QtWidgets.QLabel(parent=steganoCracker)
        self.label_number.setGeometry(QtCore.QRect(11, 391, 151, 16))
        self.label_number.setObjectName("label_number")
        self.textEdit_text = QtWidgets.QTextEdit(parent=steganoCracker)
        self.textEdit_text.setGeometry(QtCore.QRect(11, 451, 830, 82))
        self.textEdit_text.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.textEdit_text.setTabChangesFocus(True)
        self.textEdit_text.setReadOnly(False)
        self.textEdit_text.setObjectName("textEdit_text")
        self.pushButton_quit = QtWidgets.QPushButton(parent=steganoCracker)
        self.pushButton_quit.setGeometry(QtCore.QRect(761, 551, 80, 23))
        self.pushButton_quit.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.spinBox_number = QtWidgets.QSpinBox(parent=steganoCracker)
        self.spinBox_number.setGeometry(QtCore.QRect(11, 411, 75, 23))
        self.spinBox_number.setMaximum(4096)
        self.spinBox_number.setObjectName("spinBox_number")
        self.pushButton_execute = QtWidgets.QPushButton(parent=steganoCracker)
        self.pushButton_execute.setGeometry(QtCore.QRect(671, 551, 80, 23))
        self.pushButton_execute.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.pushButton_execute.setObjectName("pushButton_execute")
        self.comboBox_subpixels = QtWidgets.QComboBox(parent=steganoCracker)
        self.comboBox_subpixels.setGeometry(QtCore.QRect(11, 231, 150, 23))
        self.comboBox_subpixels.setObjectName("comboBox_subpixels")
        self.comboBox_subpixels.addItem("")
        self.comboBox_subpixels.addItem("")

        self.retranslateUi(steganoCracker)
        QtCore.QMetaObject.connectSlotsByName(steganoCracker)
        steganoCracker.setTabOrder(self.lineEdit_path, self.comboBox_operation)
        steganoCracker.setTabOrder(self.comboBox_operation, self.radioButton_rgb)
        steganoCracker.setTabOrder(self.radioButton_rgb, self.radioButton_rbg)
        steganoCracker.setTabOrder(self.radioButton_rbg, self.radioButton_grb)
        steganoCracker.setTabOrder(self.radioButton_grb, self.radioButton_gbr)
        steganoCracker.setTabOrder(self.radioButton_gbr, self.radioButton_brg)
        steganoCracker.setTabOrder(self.radioButton_brg, self.radioButton_bgr)
        steganoCracker.setTabOrder(self.radioButton_bgr, self.comboBox_pattern)
        steganoCracker.setTabOrder(self.comboBox_pattern, self.comboBox_order)
        steganoCracker.setTabOrder(self.comboBox_order, self.spinBox_number)
        steganoCracker.setTabOrder(self.spinBox_number, self.textEdit_text)
        steganoCracker.setTabOrder(self.textEdit_text, self.graphicsView_image)
        steganoCracker.setTabOrder(self.graphicsView_image, self.pushButton_execute)
        steganoCracker.setTabOrder(self.pushButton_execute, self.pushButton_quit)

    def retranslateUi(self, steganoCracker):
        _translate = QtCore.QCoreApplication.translate
        steganoCracker.setWindowTitle(_translate("steganoCracker", "steganoCracker"))
        self.label_path.setText(_translate("steganoCracker", "Specify path of the image"))
        self.label_operation.setText(_translate("steganoCracker", "Select operation"))
        self.comboBox_operation.setItemText(0, _translate("steganoCracker", "Write"))
        self.comboBox_operation.setItemText(1, _translate("steganoCracker", "Read"))
        self.pushButton_browse.setText(_translate("steganoCracker", "Browse"))
        self.radioButton_grb.setText(_translate("steganoCracker", "GRB"))
        self.radioButton_rbg.setText(_translate("steganoCracker", "RBG"))
        self.radioButton_brg.setText(_translate("steganoCracker", "BRG"))
        self.radioButton_gbr.setText(_translate("steganoCracker", "GBR"))
        self.radioButton_rgb.setText(_translate("steganoCracker", "RGB"))
        self.radioButton_bgr.setText(_translate("steganoCracker", "BGR"))
        self.label_subpixels.setText(_translate("steganoCracker", "Select subpixel layout"))
        self.label_pattern.setText(_translate("steganoCracker", "Select pattern"))
        self.comboBox_pattern.setItemText(0, _translate("steganoCracker", "Horizontal"))
        self.comboBox_pattern.setItemText(1, _translate("steganoCracker", "Vertical"))
        self.comboBox_pattern.setItemText(2, _translate("steganoCracker", "Diagonal"))
        self.label_order.setText(_translate("steganoCracker", "Select order"))
        self.comboBox_order.setItemText(0, _translate("steganoCracker", "Lowest pixel first"))
        self.comboBox_order.setItemText(1, _translate("steganoCracker", "Highest pixel first"))
        self.label_number.setText(_translate("steganoCracker", "Number of pixels to read"))
        self.pushButton_quit.setText(_translate("steganoCracker", "Quit"))
        self.pushButton_execute.setText(_translate("steganoCracker", "Execute"))
        self.comboBox_subpixels.setItemText(0, _translate("steganoCracker", "3 subpixels per pixel"))
        self.comboBox_subpixels.setItemText(1, _translate("steganoCracker", "1 subpixel per pixel"))
