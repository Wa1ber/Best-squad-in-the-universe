from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QButtonGroup, QLineEdit
from instr import *
from final_win import *
from PyQt5.QtGui import QFont
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
    def initUI(self):
        self.button_FIO = QLabel(txt_name)
        self.button_FIO_w = QLineEdit(txt_hintname)
        self.button_age = QLabel(txt_age)
        self.button_age_w = QLineEdit(txt_hintage)
        self.button_text1 = QLabel(txt_test1)
        self.button_start1 = QPushButton(txt_starttest1)
        self.button_run1 = QLineEdit(txt_hinttest1)
        self.button_text2 = QLabel(txt_test2)
        self.button_start2 = QPushButton(txt_starttest2)
        self.button_text3 = QLabel(txt_test3)
        self.button_start3 = QPushButton(txt_starttest3)
        self.button_run2 = QLineEdit(txt_hinttest2)
        self.button_run3 = QLineEdit(txt_hinttest3)
        self.button_result = QPushButton(txt_sendresults)
        self.button_time = QLabel('00:00:15')
        self.h_line = QHBoxLayout()
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line.addWidget(self.button_FIO, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_FIO_w, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_age_w, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_text1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_start1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_run1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_text2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_start2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_text3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_start3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_run2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_run3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_result, alignment = Qt.AlignCenter)
        self.r_line.addWidget(self.button_time, alignment = Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.button_result.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.fw = FinalWin()
