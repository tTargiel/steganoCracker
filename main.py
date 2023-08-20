import sys
from PyQt6.QtWidgets import QDialog, QApplication
from steganoCracker import Ui_steganoCracker
from logic import logic

# app = QApplication([])
# window = QDialog()
# ui = Ui_steganoCracker()
# ui.setupUi(window)

# window.show()
# sys.exit(app.exec())

class Window(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_steganoCracker() # Create an instance of the UI class
        self.ui.setupUi(self)
        self._connectSignals()

    def _connectSignals(self):
        self.ui.pushButton_quit.clicked.connect(lambda: QApplication.quit()) # Connect the signal to the function
        self.ui.pushButton_browse.clicked.connect(self.openFile) # Connect the signal to the function
        self.ui.lineEdit_path.returnPressed.connect(lambda: self.displayImage(self.ui.lineEdit_path.text()))
        self.ui.lineEdit_path.textChanged.connect(lambda: self.displayImage(self.ui.lineEdit_path.text()))
        self.ui.comboBox_operation.currentIndexChanged.connect(lambda: self.readOnly(self.ui.comboBox_operation.currentIndex()))
        self.ui.pushButton_execute.clicked.connect(lambda: self.readHidden(self.ui.lineEdit_path.text()))

    def writeOutput(self, text):
        logic.writeOutput(self, text)

    def openFile(self):
        logic.openFile(self)

    def displayImage(self, path):
        logic.displayImage(self, path)

    def readOnly(self, option):
        logic.readOnly(self, option)

    def readHidden(self, path):
        logic.readHidden(self, path)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()

    window.show()
    sys.exit(app.exec())