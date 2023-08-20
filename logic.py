from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFileDialog, QGraphicsScene
from PyQt6.QtGui import QPixmap
from PIL import Image

class logic():
    def writeOutput(window, text):
        window.ui.textEdit_text.setText(text) # Access the textEdit_text widget through the instance of window

    def openFile(window):
        file_dialog = QFileDialog(window)
        file_dialog.setNameFilter("Image files (*.jpg *.png *.bmp)") # Set file filters
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles() # Get the list of selected files
            if selected_files:
                selected_file = selected_files[0]
                window.ui.lineEdit_path.setText(selected_file) # Update the lineEdit_path with the selected file
                logic.displayImage(window, selected_file) # Load and display the selected image

    def displayImage(window, path):
        if path.startswith("file://"):
            path = path[7:].strip() # Remove "file://" prefix and any spaces
        window.ui.lineEdit_path.setText(path)
        pixmap = QPixmap(path)
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        window.ui.graphicsView_image.setScene(scene)
        window.ui.graphicsView_image.fitInView(scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

    def readOnly(window, option):
        window.ui.textEdit_text.setReadOnly(option)

    def readHidden(window, path):
        # Testing done in RGB layout, diagonal pattern, lowest pixel first and number of characters equal to image height
        img = Image.open(path)
        pixels = img.load()
        message = ""

        x = 0
        y = 0

        while x < img.height:
            pixel = list(pixels[x, x])
            message += str(int(pixel[y%3] & 1))
            x += 1
            y += 1

        output = ''.join(chr(int(message[i:i+8], 2)) for i in range(0, len(message), 8))
        window.ui.textEdit_text.setText(output)
