from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QButtonGroup, QLineEdit
from instr import *
app = QApplication([])
class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
    def initUI(self):
        self.button_index = QLabel(txt_index)
        self.button_workheart = QLabel(txt_workheart)
        self.line = QVBoxLayout()
        self.line.addWidget(self.button_index, alignment = Qt.AlignCenter)
        self.line.addWidget(self.button_workheart, alignment = Qt.AlignCenter)
        self.setLayout(self.line)
fw = FinalWin()
app.exec_()
