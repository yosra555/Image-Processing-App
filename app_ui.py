from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        #variables
        button_w = 290
        button_h = 90
        button_x_geometry = 1150
        button_y_geometry = 100
        
        #main window
        Form.setObjectName("Form")
        Form.resize(1500, 900)
        Form.setStyleSheet("background-color: rgb(40, 40, 40); font-size: 22px; color:#A1E3F9 ")
        Form.setWindowIcon(QtGui.QIcon("images\\icon.jpg"))
        
        
        #push buttons
        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(button_x_geometry, button_y_geometry, button_w, button_h))
        self.pushButton_1.setStyleSheet("background-color: rgb(60, 60, 60); color: #A1E3F9;")
        self.pushButton_1.setObjectName("pushButton_1")
        
        self.combobox_2 = QtWidgets.QComboBox(Form)
        self.combobox_2.setGeometry(QtCore.QRect(button_x_geometry, button_y_geometry + 120, button_w, button_h))
        self.combobox_2.setStyleSheet("background-color: rgb(60, 60, 60); color: #A1E3F9;")
        self.combobox_2.setObjectName("combobox_2")
        self.combobox_2.addItems(['         choose operation',
        'BGR_TO_GRAY', 'BGR_TO_RGB','TO_BINARY', 'BGR_TO_HSV', 'Create_Histogram', 'Histogram_Equalization',
        'Resize_To_Half', 'Resize','Crop', 'Split_B_G_R', 'Rotate_90_ClockWise', 'Rotate_90_CounterClockWise',
        'Rotate_180','Rotate_By_Degree',
        'Flip_Horizontally', 'Flip_Vertically', 'Flip_Both', 'Plot_The_Image', 'Average_Filter_blur',
        'Weighted_Filter','Gaussian_Filter', 'Minimum_Filter_erode', 'Maximum_Filter_dilate', 'Median_Filter',
        'Laplacian_Filter','LOG_Filter'])
        
        
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(button_x_geometry, button_y_geometry + 240, button_w, button_h))
        self.pushButton_3.setStyleSheet("background-color: rgb(60, 60, 60); color: #A1E3F9;")
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(button_x_geometry, button_y_geometry + 360, button_w, button_h))
        self.pushButton_4.setStyleSheet("background-color: rgb(60, 60, 60); color: #A1E3F9;")
        self.pushButton_4.setObjectName("pushButton_4")
        
        
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(button_x_geometry, 750, button_w, button_h))
        self.pushButton_5.setStyleSheet("background-color: rgb(60, 60, 60); color: #A1E3F9;")
        self.pushButton_5.setObjectName("pushButton_5")
        
        
        #create the label that will hold the photo
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 50, 1000, 800))
        self.label.setStyleSheet("background-color: rgb(60,60,60);border: rgb(215, 215, 215)")
        self.label.setObjectName("label")
    
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Image Processing"))
        self.pushButton_1.setText(_translate("Form", "load image"))
        self.pushButton_3.setText(_translate("Form", "Preview"))
        self.pushButton_4.setText(_translate("Form", "Download"))
        self.pushButton_5.setText(_translate("Form", "two images operations"))

class Ui_Form_2(object):
    def setupUi(self, Form_2):
        #variables
        button_w = 290
        button_h = 90
        button_x_geometry = 1150
        button_y_geometry = 100
            
        #main window
        Form_2.setObjectName("Form_2")
        Form_2.resize(1500, 900)
        Form_2.setStyleSheet("background-color: rgb(40, 40, 40); font-size: 22px")
        Form_2.setWindowIcon(QtGui.QIcon("images\\icon.jpg"))
        
        #push buttons
        self.pushButton_1 = QtWidgets.QPushButton(Form_2)
        self.pushButton_1.setGeometry(QtCore.QRect(button_x_geometry, button_y_geometry, button_w, button_h))
        self.pushButton_1.setStyleSheet("background-color: rgb(60, 60, 60); color: #A1E3F9;")
        self.pushButton_1.setObjectName("pushButton_1")
        
        self.pushButton_2 = QtWidgets.QPushButton(Form_2)
        self.pushButton_2.setGeometry(QtCore.QRect(button_x_geometry, button_y_geometry + 120, button_w, button_h))
        self.pushButton_2.setStyleSheet("background-color: rgb(60, 60, 60); color: #A1E3F9;")
        self.pushButton_2.setObjectName("pushButton_2")

        self.combobox_2 = QtWidgets.QComboBox(Form_2)
        self.combobox_2.setGeometry(QtCore.QRect(button_x_geometry, button_y_geometry + 240, button_w, button_h))
        self.combobox_2.setStyleSheet("background-color: rgb(60, 60, 60); color: #A1E3F9;")
        self.combobox_2.setObjectName("combobox_2")
        self.combobox_2.addItems(['         choose operation',
        'Addition', 'Subtraction'])
        
        self.pushButton_3 = QtWidgets.QPushButton(Form_2)
        self.pushButton_3.setGeometry(QtCore.QRect(button_x_geometry, button_y_geometry + 360, button_w, button_h))
        self.pushButton_3.setStyleSheet("background-color: rgb(60, 60, 60); color: #A1E3F9;")
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_4 = QtWidgets.QPushButton(Form_2)
        self.pushButton_4.setGeometry(QtCore.QRect(button_x_geometry, button_y_geometry + 480, button_w, button_h))
        self.pushButton_4.setStyleSheet("background-color: rgb(60, 60, 60); color: #A1E3F9;")
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.pushButton_5 = QtWidgets.QPushButton(Form_2)
        self.pushButton_5.setGeometry(QtCore.QRect(button_x_geometry, 750, button_w, button_h))
        self.pushButton_5.setStyleSheet("background-color: rgb(60, 60, 60); color: #A1E3F9;")
        self.pushButton_5.setObjectName("pushButton_5")
        
        #the first label
        self.label_1 = QtWidgets.QLabel(Form_2)
        self.label_1.setGeometry(QtCore.QRect(40, 40, 1000, 400))
        self.label_1.setStyleSheet("background-color: rgb(60,60,60);border: rgb(215, 215, 215)")
        self.label_1.setObjectName("label_1")
        #the second label
        self.label_2 = QtWidgets.QLabel(Form_2)
        self.label_2.setGeometry(QtCore.QRect(40, 460, 1000, 400))
        self.label_2.setStyleSheet("background-color: rgb(60,60,60);border: rgb(215, 215, 215)")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form_2)
        QtCore.QMetaObject.connectSlotsByName(Form_2)
    

    def retranslateUi(self, Form_2):
        _translate = QtCore.QCoreApplication.translate
        Form_2.setWindowTitle(_translate("Form_2", "Image Processing"))
        self.pushButton_1.setText(_translate("Form_2", "load the first image"))
        self.pushButton_2.setText(_translate("Form_2", "load the second image"))
        self.pushButton_3.setText(_translate("Form_2", "Preview"))
        self.pushButton_4.setText(_translate("Form_2", "Download"))
        self.pushButton_5.setText(_translate("Form_2", "one image operations"))


