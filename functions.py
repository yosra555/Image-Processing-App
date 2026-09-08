from app_ui import Ui_Form, Ui_Form_2
import cv2 as cv
import os
from pathlib import Path
import sys
import numpy as np
import imutils
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QInputDialog, QVBoxLayout, QSpinBox

#variabels
input_image_path = ''
input_image_path_2 = ''
output_image = None 
output_image_2 = None
output_image_3 = None
angle = None
width, height = None, None
rows_start, rows_end, columns_start, columns_end = None, None, None, None
##########

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)

Form_2 = QtWidgets.QWidget()
ui_2 = Ui_Form_2()
ui_2.setupUi(Form_2)

stacked_widget = QtWidgets.QStackedWidget()# is used to switch between screens
stacked_widget.addWidget(Form)
stacked_widget.addWidget(Form_2)

#load the photo into the label 
def load_image(label_widget):
    global input_image_path, input_image_path_2
    path = QFileDialog.getOpenFileName(None, 'choose an image', None, filter= 'Images (*.jpeg *.jpg *.bmp *.png)')
    if str(label_widget) == str(ui_2.label_2):

        input_image_path_2 = path[0] 
        pixmap = QPixmap(input_image_path_2).scaled(label_widget.size(), QtCore.Qt.KeepAspectRatio)

    else:
        input_image_path = path[0]
        pixmap = QPixmap(input_image_path).scaled(label_widget.size(), QtCore.Qt.KeepAspectRatio)
    
    label_widget.setPixmap(pixmap)

#preview the output of cv2 library 
def preview_cv_output():
    global selected_filter 
    selected_filter = ui.combobox_2.currentText()
    if selected_filter == 'Split_B_G_R':
        cv.imshow('Blue', output_image)
        cv.imshow('Green', output_image_2)
        cv.imshow('Red', output_image_3)
    else:
        cv.imshow('Image Preview', output_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def preview_plot_output():
    plt.show()
 
def download_image():
    def show_message():
        downloaded_msg = QMessageBox()
        downloaded_msg.setText('Image was successfully downloaded')
        downloaded_msg.setStandardButtons(QMessageBox.Ok)
        downloaded_msg.setStyleSheet('background-color: rgb(60, 60, 60); color: #A1E3F9; font-size: 22px')
        downloaded_msg.exec_()

    downloads_path = str(Path.home() / "Downloads")

    if output_image is not None and selected_filter == 'Split_B_G_R':
        cv.imwrite(os.path.join(downloads_path, 'Blue Image.jpg'), output_image)
        cv.imwrite(os.path.join(downloads_path, 'Green Image.jpg'), output_image_2)
        cv.imwrite(os.path.join(downloads_path, 'Red Image.jpg'), output_image_3)
        show_message()
    elif output_image is not None:
        cv.imwrite(os.path.join(downloads_path, 'processed image.jpg'), output_image)
        show_message()
    

def gotoUi_1():
    stacked_widget.setCurrentIndex(0)
        
def gotoUi_2():
    stacked_widget.setCurrentIndex(1)

#operations on images
def BGR_TO_GRAY():
    global output_image
    image = cv.imread(input_image_path)
    output_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

def BGR_TO_RGB():
    global output_image
    image = cv.imread(input_image_path)
    output_image= cv.cvtColor(image, cv.COLOR_BGR2RGB)

def TO_BINARY():
    global output_image
    image = cv.imread(input_image_path)
    if(len(image.shape) == 3):
        gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    else:
        gray_image = image
    threshold, output_image =  cv.threshold(gray_image, 127, 255, cv.THRESH_BINARY)

def BGR_TO_HSV():
    global output_image
    image = cv.imread(input_image_path)
    output_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

def Create_Histogram():
    image = cv.imread(input_image_path)
    gray_image = cv.cvtColor(image, cv.COLOR_RGB2BGRA)
    histogram = cv.calcHist(gray_image, [0], None, [256], [0, 256])# 0 means calculating the histogram for grayscale images
    plt.plot(histogram)
    plt.title('GrayScale Histogram')
    plt.xlabel('pixel values')
    plt.ylabel('frequency')
    plt.xlim([0, 256])

def Histogram_Equalization():
    image = cv.imread(input_image_path)
    gray_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    equalized_image = cv.equalizeHist(gray_image)
    histogram_of_equalizde_image = cv.calcHist(equalized_image, [0], None, [256], [0, 255])
    plt.figure()
    plt.imshow(equalized_image, cmap='gray')
    plt.title('equalized image')
    plt.figure()
    plt.plot(histogram_of_equalizde_image)
    plt.title('histogram of equalized image')
    
def Addition():
    global output_image
    image1 = cv.imread(input_image_path)
    image2 = cv.imread(input_image_path_2)
    image1 = cv.resize(image1, (900, 800))
    image2 = cv.resize(image2, (900, 800))
    output_image = cv.add(image1, image2)
    
def Subtraction():
    global output_image
    image1 = cv.imread(input_image_path)
    image2 = cv.imread(input_image_path_2)
    image1 = cv.resize(image1, (900, 800))
    image2 = cv.resize(image2, (900, 800))
    output_image = cv.subtract(image1, image2)

def Resize_To_Half():
    global output_image
    image = cv.imread(input_image_path)
    h, w = image.shape[0], image.shape[1]
    output_image = cv.resize(image, (w //2, h //2), interpolation = cv.INTER_NEAREST)

def Resize():
    global output_image
    image = cv.imread(input_image_path)
    output_image = cv.resize(image, (width, height))

def Crop():
    global output_image
    image = cv.imread(input_image_path)
    output_image = image[rows_start:rows_end, columns_start:columns_end]

def Split_B_G_R():
    global output_image, output_image_2 , output_image_3
    image = cv.imread(input_image_path)
    output_image, output_image_2, output_image_3 = cv.split(image)

def Rotate_90_ClockWise():
    global output_image
    image = cv.imread(input_image_path)
    output_image = cv.rotate(image, cv.ROTATE_90_CLOCKWISE)

def Rotate_90_CounterClockWise():
    global output_image
    image = cv.imread(input_image_path)
    output_image = cv.rotate(image, cv.ROTATE_90_COUNTERCLOCKWISE)

def Rotate_180():
    global output_image
    image = cv.imread(input_image_path)
    output_image = cv.rotate(image, cv.ROTATE_180)

def Rotate_By_Degree():
    global output_image
    image = cv.imread(input_image_path)
    output_image = imutils.rotate_bound(image, angle)

def Flip_Horizontally():
    global output_image
    image = cv.imread(input_image_path)
    output_image = cv.flip(image, 1)

def Flip_Vertically():
    global output_image
    image = cv.imread(input_image_path)
    output_image = cv.flip(image, 0)

def Flip_Both():
    global output_image
    image = cv.imread(input_image_path)
    output_image = cv.flip(image, -1)

def Plot_The_Image():
    image = cv.imread(input_image_path)
    RGB_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    plt.imshow(RGB_image)
    plt.title("Plotted Image")

def Average_Filter_blur():
    global output_image
    image = cv.imread(input_image_path)
    output_image = cv.blur(image, (3,3))

def Weighted_Filter():
    global output_image
    image = cv.imread(input_image_path)
    kernel = np.array([[1,2,1],[2,4,2],[1,2,1]])
    k= kernel /np.sum(kernel)
    output_image = cv.filter2D(image, -1, k)

def Gaussian_Filter():
    global output_image
    image = cv.imread(input_image_path)
    output_image = cv.GaussianBlur(image, (5, 5), 0)

def Minimum_Filter_erode():
    global output_image
    image = cv.imread(input_image_path)
    kernel = np.ones((5,5), np.uint8)
    output_image = cv.erode(image, kernel)


def Maximum_Filter_dilate():
    global output_image
    image = cv.imread(input_image_path)
    kernel = np.ones((5,5), np.uint8)
    output_image = cv.dilate(image, kernel)

def Median_Filter():
    global output_image
    image = cv.imread(input_image_path)
    output_image = cv.medianBlur(image, 5)

def Laplacian_Filter():
    global output_image
    image = cv.imread(input_image_path)
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    sharppening = cv.Laplacian(image, -1, ksize=5)
    output_image = cv.addWeighted(image, 0.9, sharppening,0.9 ,0)

def LOG_Filter():
    #Laplacian of gaussian filter
    global output_image
    image = cv.imread(input_image_path)
    image = cv.GaussianBlur(image, (5,5), 0)
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    sharppening = cv.Laplacian(image_gray, -1, ksize=5)
    output_image = cv.addWeighted(image_gray, 0.9, sharppening, 0.9, 0)

#the first widget  
#push buttons functions
ui.pushButton_1.clicked.connect(lambda: load_image(ui.label))
#to get an angle from the user if they choose rotate_by_angle method
def get_angle():
        global angle
        dialog = QInputDialog()
        dialog.setStyleSheet(" QInputDialog {background-color: rgb(60, 60, 60);color: #A1E3F9; font-size : 20px}")
        dialog.setWindowIcon(QtGui.QIcon("images\\icon.jpg"))
        selected_filter = ui.combobox_2.currentText()
        print(f'selected_filter : {selected_filter}')
        if selected_filter == 'Rotate_By_Degree':
            input_angle, ok = dialog.getInt(Form, "Get Angle", "Angle (degrees):", 0, 0, 360, 1)
            if ok:
                angle = input_angle
ui.combobox_2.currentTextChanged.connect(get_angle)
#to get width and height from the user if they choose Resize method
def get_size():
    selected_filter = ui.combobox_2.currentText()
    if selected_filter == 'Resize':
        layout = QtWidgets.QDialog()
        layout.setWindowTitle('Get Inputs')
        layout.setWindowIcon(QtGui.QIcon("images\\icon.jpg"))
        layout.setStyleSheet('background-color: rgb(60, 60, 60); color:#A1E3F9; font-size: 20px')
        box = QVBoxLayout()
        label = QtWidgets.QLabel('Width: ')
        input_1 = QtWidgets.QLineEdit()
        label_2 = QtWidgets.QLabel('Height: ')
        input_2 = QtWidgets.QLineEdit()
        button = QtWidgets.QPushButton('OK')
        items_list = [label, input_1, label_2, input_2, button]
        for item in items_list:
            box.addWidget(item)
        layout.setLayout(box)    
        
        def set_values():
            global width, height
            width = int(input_1.text())
            height = int(input_2.text())
           
            layout.accept()

        button.clicked.connect(set_values)
        layout.exec_()

ui.combobox_2.currentTextChanged.connect(get_size)

#to get rows(start, end) and columns(start, end) for cropping an image 
def get_rows_columns():
    selected_filter = ui.combobox_2.currentText()
    if selected_filter == 'Crop':
        layout = QtWidgets.QDialog()
        layout.setWindowTitle('Get Inputs')
        layout.setWindowIcon(QtGui.QIcon("images\\icon.jpg"))
        layout.setStyleSheet('background-color: rgb(60, 60, 60); color:#A1E3F9; font-size: 20px')
        box = QVBoxLayout()
        label = QtWidgets.QLabel('rows_start, rows_end: ')
        input_1 = QtWidgets.QLineEdit()
        input_1.setText('eg: 500,900')
        label_2 = QtWidgets.QLabel('columns_start, columns_end: ')
        input_2 = QtWidgets.QLineEdit()
        input_2.setText('eg: 100,600')
        button = QtWidgets.QPushButton('OK')
        items_list = [label, input_1, label_2, input_2, button]
        for item in items_list:
            box.addWidget(item)
        layout.setLayout(box)    
        
        def set_values():
            global rows_start, rows_end, columns_start, columns_end
            list = (input_1.text()).split(',')
            rows_start, rows_end = int(list[0]), int(list[1])
            list = (input_2.text()).split(',')
            columns_start, columns_end = int(list[0]), int(list[1])
           
            layout.accept()

        button.clicked.connect(set_values)
        layout.exec_()

ui.combobox_2.currentTextChanged.connect(get_rows_columns)
def ui1_button_3_clicked():
    selected_filter = ui.combobox_2.currentText()
    print(selected_filter)
    if input_image_path != '':
        if selected_filter != ui.combobox_2.itemText(0):
            list = ['Create_Histogram', 'Histogram_Equalization','Plot_The_Image']
            if selected_filter in list:
                globals()[selected_filter]()
                preview_plot_output()
            else:
                globals()[selected_filter]()
                preview_cv_output()
       
        
ui.pushButton_3.clicked.connect(ui1_button_3_clicked)
ui.pushButton_4.clicked.connect(download_image)
ui.pushButton_5.clicked.connect(gotoUi_2)

#the second widget
#push buttons functions
def ui2_button_3_clicked():
    selected_filter = ui_2.combobox_2.currentText()
    if selected_filter != ui_2.combobox_2.itemText(0):
        globals()[selected_filter]()
        preview_cv_output()

ui_2.pushButton_1.clicked.connect(lambda: load_image(ui_2.label_1))
ui_2.pushButton_2.clicked.connect(lambda: load_image(ui_2.label_2))
ui_2.pushButton_3.clicked.connect(ui2_button_3_clicked)
ui_2.pushButton_4.clicked.connect(download_image)
ui_2.pushButton_5.clicked.connect(gotoUi_1)

#stacked widget
stacked_widget.setFixedSize(1500, 900)
stacked_widget.setWindowIcon(QtGui.QIcon("images\\icon.jpg"))
stacked_widget.setWindowTitle("Image Processing App")
stacked_widget.show()
sys.exit(app.exec_())