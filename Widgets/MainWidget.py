from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtCore import Slot

class MainWidget(QWidget):
    
    def __init__(self):
        super().__init__() 
        self.labelPrueba = QLabel('<font color=green size=40>Hola</font>')
        self.button = QPushButton('Pulsar')
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.labelPrueba)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.pulsarBoton)
    
    @Slot()
    def pulsarBoton(self):
        self.labelPrueba.setText('<font color=red size=40>Buenas</font>')