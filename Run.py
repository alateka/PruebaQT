import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# App modules
from Widgets.MainWidget import MainWidget

# Main window class
class MainWindow(QMainWindow):
  
    # It load the main window
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Prueba')
        self.mainWidget = MainWidget()
        self.setCentralWidget(self.mainWidget)

# Start application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())