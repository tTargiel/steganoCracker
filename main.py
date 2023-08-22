import sys
from PyQt6.QtWidgets import QDialog, QApplication, QRadioButton
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

        self.selected_operation = 0 # Class variable to keep track of selected operation
        self.selected_radio_button = None # Class variable to keep track of selected radio button
        self.selected_pattern = 0 # Class variable to keep track of selected pattern
        self.selected_subpixels = 0 # Class variable to keep track of selected subpixels
        self.variable = 1 # Change point of length variance calculation
        self.selected_order = 0 # Class variable to keep track of selected order
        self.ui.label_number.setVisible(0)
        self.ui.spinBox_number.setVisible(0)

        self._connectSignals()

    def _connectSignals(self):
        self.ui.pushButton_quit.clicked.connect(lambda: QApplication.quit()) # Connect the signal to the function
        self.ui.pushButton_browse.clicked.connect(self.openFile)
        self.ui.lineEdit_path.returnPressed.connect(lambda: self.displayImage(self.ui.lineEdit_path.text()))
        self.ui.lineEdit_path.textChanged.connect(lambda: self.displayImage(self.ui.lineEdit_path.text()))
        self.ui.comboBox_operation.currentIndexChanged.connect(lambda: self.readOperation(self.ui.comboBox_operation.currentIndex()))

        # Connect radio buttons to a function that handles their clicks
        self.ui.radioButton_rgb.animateClick() # Makes sure to emit clicked signal on RGB
        self.ui.radioButton_rgb.clicked.connect(self.radio_button_clicked)
        self.ui.radioButton_rbg.clicked.connect(self.radio_button_clicked)
        self.ui.radioButton_grb.clicked.connect(self.radio_button_clicked)
        self.ui.radioButton_gbr.clicked.connect(self.radio_button_clicked)
        self.ui.radioButton_brg.clicked.connect(self.radio_button_clicked)
        self.ui.radioButton_bgr.clicked.connect(self.radio_button_clicked)

        self.ui.comboBox_pattern.currentIndexChanged.connect(lambda: self.pattern_changed(self.ui.comboBox_pattern.currentIndex()))
        self.ui.comboBox_subpixels.currentIndexChanged.connect(lambda: self.subpixels_changed(self.ui.comboBox_subpixels.currentIndex()))
        self.ui.comboBox_order.currentIndexChanged.connect(lambda: self.order_changed(self.ui.comboBox_order.currentIndex()))

        self.ui.pushButton_execute.clicked.connect(lambda: self.executeButton(self.ui.lineEdit_path.text()))

    def writeOutput(self, text):
        logic.writeOutput(self, text)

    def openFile(self):
        logic.openFile(self)

    def displayImage(self, path):
        logic.displayImage(self, path)

    def readOperation(self, option):
        self.selected_operation = option
        logic.readOperation(self, option)

    def readHidden(self, path):
        logic.readHidden(self, path)

    def radio_button_clicked(self):
        sender = self.sender() # Get the radio button that triggered the signal
        if isinstance(sender, QRadioButton):
            self.selected_radio_button = sender # Update the selected radio button

    def pattern_changed(self, option):
        self.selected_pattern = option

    def subpixels_changed(self, option):
        self.variable = 1 if option == 0 else 3
        self.selected_subpixels = option

    def order_changed(self, option):
        self.selected_order = option

    def executeButton(self, path):
        radio_text = self.selected_radio_button.text() # Get the text of the selected radio button
        pattern_text = self.selected_pattern
        order_text = self.selected_order
        subpixels_text = self.selected_subpixels
        variable = self.variable

        if self.selected_operation == 0:
            text = self.ui.textEdit_text.toPlainText() # Get the text from the textEdit_text
            length = len(text) # Calculate the length of the text
            logic.writeHidden(self, path, radio_text, pattern_text, order_text, length, text, subpixels_text, variable)
        else:
            length = self.ui.spinBox_number.value() * 3 - variable
            logic.readHidden(self, path, radio_text, pattern_text, order_text, length, subpixels_text, variable)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()

    window.show()
    sys.exit(app.exec())