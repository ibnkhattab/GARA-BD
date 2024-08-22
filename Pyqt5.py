
import sys
from PyQt5.QtWidgets import QApplication , QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Garage BAGAYA Dramane")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("Img/Qt/WinPic_01.jpeg"))
        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()











