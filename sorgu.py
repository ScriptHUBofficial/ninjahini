######################### QT LIB #########################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import socket
from threading import Thread

class Ui_sorgu( QtWidgets.QMainWindow ):
    signal_tablo = pyqtSignal( str )
    def __init__(self): #*****
        super().__init__() #*****

        self.setupUi() #*****

        

    def sayfakuluct(self):
        self.showMinimized()

    def sayfakapat(self):
        self.close()

    def tablotemizle(self):                
        self.sorgusonuc.clear()


    def client_program(self):
        host = "127.0.0.1"
        port = 5000

        client_socket = socket.socket()
        client_socket.connect((host, port))

        isimi = self.linedit1.text()
        soyisimi = self.linedit2.text()
        dogum_tarihi = self.linedit3.text()
        sehir = self.linedit4.text()
        kimlikno = self.linedit5.text()

        data_list = [ isimi , soyisimi ,dogum_tarihi , sehir , kimlikno]
        data_str = '|'.join(data_list)
        client_socket.send(data_str.encode("utf-8"))

        while True:

            sorgu_sonucu = client_socket.recv(1024).decode("utf-8")
            self.signal_tablo.emit(sorgu_sonucu)

            if not sorgu_sonucu:
                print("server is down")
                break
        client_socket.close()

    def tabloya_yaz(self, sorgu_sonucu):
        try: 
            sorgular = sorgu_sonucu.split('|')
            print(sorgular)
            row = self.sorgusonuc.rowCount()
            print(row)
            self.sorgusonuc.insertRow(row)
            for col in range ( len(sorgular) ):
                self.sorgusonuc.setItem( row, col, QTableWidgetItem((sorgular)[col]))
        except Exception as error:
            print(error)

    def ananisikim(self):

        self.sorgusonuc.setRowCount(0)

        t1=Thread(target=self.client_program)
        t1.start()       

    def setupUi(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setObjectName("sorgu")
        self.resize(1500, 900)
        self.setMaximumSize(QtCore.QSize(1500, 900))
        self.setStyleSheet("\n"
"QMainWindow {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QDialog {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QColorDialog {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTextEdit {\n"
"    background-color:#1e1d23;\n"
"    color: #a9b7c6;\n"
"}\n"
"QPlainTextEdit {\n"
"    selection-background-color:#23dae9;\n"
"    background-color:#1e1d23;\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-width: 1px;\n"
"    color: #a9b7c6;\n"
"}\n"
"\n"
"QToolButton {\n"
"    border-radius: 15px;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #23dae9;\n"
"    border-bottom-width: 1px;\n"
"    border-radius: 15px;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover{\n"
"    border-width: 2px; border-radius: 15px;\n"
"    border-radius: 15px;\n"
"    border-color: #23dae9;\n"
"\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"    border-style: solid;\n"
"\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton::default{\n"
"    border-style: inset;\n"
"\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding-bottom: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"    border-width: 2px; border-radius: 15px;\n"
"    border-color: #23dae9;\n"
"    border-style: inset;\n"
"    padding: 0 8px;\n"
"    color: #FFF;\n"
"    background:rgb(36,36,36);\n"
"    selection-background-color:#23dae9;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid #23dae9\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border:2px solid #23dae9\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"    color: #a9b7c6;\n"
"}\n"
"QLCDNumber {\n"
"    color: #23dae9;\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color:#1e1d23;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #23dae9;\n"
"    border-radius: 5px;\n"
"}\n"
"QMenuBar {\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenuBar::item {\n"
"    color: #a9b7c6;\n"
"      spacing: 3px;\n"
"      padding: 1px 4px;\n"
"      background: #1e1d23;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"      background:#1e1d23;\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: #23dae9;\n"
"    border-bottom-color: transparent;\n"
"    border-left-width: 2px;\n"
"    color: #FFFFFF;\n"
"    padding-left:15px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenu::item {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding-left:17px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenu{\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(77,77,77);\n"
"        background-color:#1e1d23;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #808086;\n"
"    padding: 3px;\n"
"    margin-left:3px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #23dae9;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-left: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-left:3px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: rgb(87, 97, 106);\n"
"    background-color:#1e1d23;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #23dae9;\n"
"    color: #a9b7c6;\n"
"    background-color: #23dae9;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #23dae9;\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QRadioButton {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #23dae9;\n"
"    color: #a9b7c6;\n"
"    background-color: #23dae9;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #23dae9;\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDoubleSpinBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QTimeEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDateTimeEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDateEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QComboBox {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"}\n"
"QComboBox:editable {\n"
"    background: #1e1d23;\n"
"    color: #a9b7c6;\n"
"    selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"    selection-color: #FFFFFF;\n"
"    selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"}\n"
"QFontComboBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: #23dae9;\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background: #23dae9;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 14px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    height: 14px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: white;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: #23dae9;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background: #23dae9;\n"
"}")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.kucult = QtWidgets.QRadioButton(self.centralwidget)
        self.kucult.setGeometry(QtCore.QRect(1430, 10, 16, 17))
        self.kucult.setStyleSheet("QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color:  rgb(255, 255, 0);\n"
"    color:  rgb(255, 255, 0);\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color:  rgb(255, 255, 0);\n"
"    color:  rgb(255, 255, 0);\n"
"    background-color:  rgb(255, 255, 0);\n"
"}")
        self.kucult.setText("")
        self.kucult.setObjectName("kucult")
        self.buyult = QtWidgets.QRadioButton(self.centralwidget)
        self.buyult.setGeometry(QtCore.QRect(1450, 10, 16, 17))
        self.buyult.setStyleSheet("QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(0, 255, 0);\n"
"    color: rgb(0, 255, 0);\n"
"    background-color: rgb(0, 255, 0);\n"
"}\n"
"\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(0, 255, 0);\n"
"    color: rgb(0, 255, 0);\n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.buyult.setText("")
        self.buyult.setObjectName("buyult")
        self.kapat = QtWidgets.QRadioButton(self.centralwidget)
        self.kapat.setGeometry(QtCore.QRect(1470, 10, 16, 17))
        self.kapat.setStyleSheet("QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(208, 0, 0);\n"
"    color: rgb(208, 0, 0);\n"
"    background-color: rgb(208, 0, 0);\n"
"}\n"
"\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(208, 0, 0);\n"
"    color: rgb(208, 0, 0);\n"
"    background-color: rgb(208, 0, 0);\n"
"}")
        self.kapat.setText("")
        self.kapat.setObjectName("kapat")
        self.sorgusonuc = QtWidgets.QTableWidget(self.centralwidget)
        self.sorgusonuc.setGeometry(QtCore.QRect(280, 90, 1201, 791))
        self.sorgusonuc.setColumnCount(15)
        self.sorgusonuc.setObjectName("sorgusonuc")
        self.sorgusonuc.setStyleSheet("QHeaderView::section  {\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QTableView\n"
"{\n"
"    border: 1px solid #444;\n"
"    gridline-color: #6c6c6c;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"\n"
"QTableView, QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"    color:rgb(0, 255, 255)\n"
"}\n"
"\n"
"QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {\n"
"    background: #78879b;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color: #3A3939;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"}")
        self.backtoenu = QtWidgets.QPushButton(self.centralwidget)
        self.backtoenu.setGeometry(QtCore.QRect(20, 20, 101, 21))
        self.backtoenu.setObjectName("backtoenu")
        self.yirmiiki = QtWidgets.QRadioButton(self.centralwidget)
        self.yirmiiki.setGeometry(QtCore.QRect(10, 460, 82, 17))
        self.yirmiiki.setObjectName("yirmiiki")
        self.ikibinonbes = QtWidgets.QRadioButton(self.centralwidget)
        self.ikibinonbes.setGeometry(QtCore.QRect(10, 480, 82, 17))
        self.ikibinonbes.setObjectName("ikibinonbes")
        self.egmonyedi = QtWidgets.QRadioButton(self.centralwidget)
        self.egmonyedi.setGeometry(QtCore.QRect(10, 500, 82, 17))
        self.egmonyedi.setObjectName("egmonyedi")
        self.telno = QtWidgets.QRadioButton(self.centralwidget)
        self.telno.setGeometry(QtCore.QRect(10, 520, 82, 17))
        self.telno.setObjectName("telno")
        self.clearboard = QtWidgets.QPushButton(self.centralwidget)
        self.clearboard.setGeometry(QtCore.QRect(100, 460, 75, 23))
        self.clearboard.setObjectName("clearboard")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(190, 460, 75, 23))
        self.search.setObjectName("search")
        self.scriptlogo = QtWidgets.QLabel(self.centralwidget)
        self.scriptlogo.setGeometry(QtCore.QRect(16, 615, 251, 261))
        self.scriptlogo.setStyleSheet("")
        self.scriptlogo.setText("")
        self.scriptlogo.setObjectName("scriptlogo")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 600, 261, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(90, 570, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(97, 90, 171, 360))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.linedit1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.linedit1.setObjectName("linedit1")
        self.verticalLayout.addWidget(self.linedit1)
        self.linedit2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.linedit2.setObjectName("linedit2")
        self.verticalLayout.addWidget(self.linedit2)
        self.linedit3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.linedit3.setObjectName("linedit3")
        self.verticalLayout.addWidget(self.linedit3)
        self.linedit4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.linedit4.setObjectName("linedit4")
        self.verticalLayout.addWidget(self.linedit4)
        self.linedit5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.linedit5.setObjectName("linedit5")
        self.verticalLayout.addWidget(self.linedit5)
        self.linedit6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.linedit6.setObjectName("linedit6")
        self.verticalLayout.addWidget(self.linedit6)
        self.linedit7 = QtWidgets.QLineEdit(self.layoutWidget)
        self.linedit7.setObjectName("linedit7")
        self.verticalLayout.addWidget(self.linedit7)
        self.linedit8 = QtWidgets.QLineEdit(self.layoutWidget)
        self.linedit8.setObjectName("linedit8")
        self.verticalLayout.addWidget(self.linedit8)
        self.linedit9 = QtWidgets.QLineEdit(self.layoutWidget)
        self.linedit9.setObjectName("linedit9")
        self.verticalLayout.addWidget(self.linedit9)
        self.linedit10 = QtWidgets.QLineEdit(self.layoutWidget)
        self.linedit10.setObjectName("linedit10")
        self.verticalLayout.addWidget(self.linedit10)
        self.linedit12 = QtWidgets.QLineEdit(self.layoutWidget)
        self.linedit12.setObjectName("linedit12")
        self.verticalLayout.addWidget(self.linedit12)
        self.linedit11 = QtWidgets.QLineEdit(self.layoutWidget)
        self.linedit11.setObjectName("linedit11")
        self.verticalLayout.addWidget(self.linedit11)
        self.linedit13 = QtWidgets.QLineEdit(self.layoutWidget)
        self.linedit13.setObjectName("linedit13")
        self.verticalLayout.addWidget(self.linedit13)
        self.linedit14 = QtWidgets.QLineEdit(self.layoutWidget)
        self.linedit14.setObjectName("linedit14")
        self.verticalLayout.addWidget(self.linedit14)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 90, 81, 361))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.setCentralWidget(self.centralwidget)

        self.kapat.clicked.connect(self.sayfakapat)
        self.kucult.clicked.connect(self.sayfakuluct)
        self.search.clicked.connect(self.ananisikim)
        self.clearboard.clicked.connect(self.tablotemizle)


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.signal_tablo.connect( self.tabloya_yaz)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("sorgu", "MainWindow"))
        self.backtoenu.setText(_translate("sorgu", "<-- back to menu"))
        self.yirmiiki.setText(_translate("sorgu", "test"))
        self.ikibinonbes.setText(_translate("sorgu", "test"))
        self.egmonyedi.setText(_translate("sorgu", "test"))
        self.telno.setText(_translate("sorgu", "test"))
        self.clearboard.setText(_translate("sorgu", "TEMİZLE"))
        self.search.setText(_translate("sorgu", "ARA"))
        self.label_16.setText(_translate("sorgu", "VSCRİPT"))
        self.label_14.setText(_translate("sorgu", "Name :"))
        self.label.setText(_translate("sorgu", "LastName :"))
        self.label_13.setText(_translate("sorgu", "DOGUM T. :"))
        self.label_2.setText(_translate("sorgu", "SEHİR :"))
        self.label_12.setText(_translate("sorgu", "TC NO :"))
        self.label_3.setText(_translate("sorgu", "İSİM :"))
        self.label_11.setText(_translate("sorgu", "İSİM :"))
        self.label_4.setText(_translate("sorgu", "İSİM :"))
        self.label_5.setText(_translate("sorgu", "İSİM :"))
        self.label_10.setText(_translate("sorgu", "İSİM :"))
        self.label_6.setText(_translate("sorgu", "İSİM :"))
        self.label_9.setText(_translate("sorgu", "İSİM :"))
        self.label_7.setText(_translate("sorgu", "İSİM :"))
        self.label_8.setText(_translate("sorgu", "İSİM :"))

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_sorgu()
    ui.show()
    sys.exit(app.exec_())
