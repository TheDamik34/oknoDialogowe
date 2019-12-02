import sys

import PyQt5.QtCore
from PyQt5.QtWidgets import (QWidget, QGridLayout, QMenu, QLabel, QMenuBar, QMainWindow, QPushButton, QApplication, QTextEdit, QAction, QVBoxLayout, QHBoxLayout, QRadioButton, QFileDialog,
                             QSpinBox, qApp)
from PyQt5.QtGui import QIcon

class Okno(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')

        labelcentral = QLabel()
        labelcentral.setStyleSheet('background-color: #90ee90')

        acction1 = QAction('&Nazwa okna glownego', self)
        acction2 = QAction('&Ustaw kola', self)
        acction3 = QAction('&Zmien Ikone', self)

        fileMenu.addAction(acction1)
        fileMenu.addAction(acction2)
        fileMenu.addAction(acction3)

        self.setWindowIcon(QIcon('icons8-binary-file-96.png'))
        self.setCentralWidget(labelcentral)
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Statusbar')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Okno()
    sys.exit(app.exec_())