import re
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFileDialog, QGraphicsScene, QMessageBox
from PyQt6.QtGui import QPixmap
from PIL import Image
from urllib.parse import unquote

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
                try:
                    logic.displayImage(window, selected_file) # Load and display the selected image
                except:
                    logic.writeOutput(window, "Something went wrong.")

    def displayImage(window, path):
        path = unquote(path.strip())
        if logic.validate_path(window, path):  # Check if the path is valid
            if path.startswith("file://"):
                path = path[7:]  # Remove "file://" prefix
            window.ui.lineEdit_path.setText(path)
            pixmap = QPixmap(path)
            scene = QGraphicsScene()
            scene.addPixmap(pixmap)
            window.ui.graphicsView_image.setScene(scene)
            window.ui.graphicsView_image.fitInView(scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
            logic.writeOutput(window, "")
        elif path == "":
            logic.writeOutput(window, "")
        else:
            # QMessageBox.warning(window, "Invalid File Path", "The file path is not valid.")
            logic.writeOutput(window, "The file path is not valid. Are you sure, you already specified image file?")

    def validate_path(self, path):
        regex_pattern = r"^(.+)\/([^\/]+)\.(ppm|png|jpg|jpeg|gif|tiff|bmp)$"
        return re.match(regex_pattern, path, re.IGNORECASE)

    def readOperation(window, option):
        window.ui.textEdit_text.setReadOnly(option)
        window.ui.label_number.setVisible(option)
        window.ui.spinBox_number.setVisible(option)

    def showNumber(window, option):
        window.ui.textEdit_text.setReadOnly(option)

    def readHidden(window, path, radio_text, pattern_text, order_text, length):
        if path:
            try:
                img = Image.open(path)
                pixels = img.load()
                message = ""

                # Initialize the starting coordinates based on order_text
                start_x = 0
                start_y = 0
                if order_text == 1:
                    start_x = img.width - 3
                    start_y = img.height - 3

                # Initialize the iteration step based on pattern_text
                step_x = 0
                step_y = 0
                if pattern_text == 0:
                    step_x = 3
                elif pattern_text == 1:
                    step_y = 3
                elif pattern_text == 2:
                    step_x = 3
                    step_y = 3

                # Determine whether step will be used
                is_x = 0
                if step_x == 3:
                    is_x = 1
                
                is_y = 0
                if step_y == 3:
                    is_y = 1

                # Iterate through the 2D array based on pattern_text and order_text
                for i in range(length):
                    x = start_x + i * step_x
                    y = start_y + i * step_y
                    
                    # Adjust x and y based on order_text
                    if order_text == 1:
                        x -= i * step_x
                        y -= i * step_y

                    if radio_text == "RGB":
                        message += str(format(pixels[x, y][0] & 1, 'b'))
                        message += str(format(pixels[x+(1*is_x), y+(1*is_y)][1] & 1, 'b'))
                        message += str(format(pixels[x+(2*is_x), y+(2*is_y)][2] & 1, 'b'))

                    elif radio_text == "RBG":
                        message += str(format(pixels[x, y][0] & 1, 'b'))
                        message += str(format(pixels[x+(1*is_x), y+(1*is_y)][2] & 1, 'b'))
                        message += str(format(pixels[x+(2*is_x), y+(2*is_y)][1] & 1, 'b'))

                    elif radio_text == "GRB":
                        message += str(format(pixels[x, y][1] & 1, 'b'))
                        message += str(format(pixels[x+(1*is_x), y+(1*is_y)][0] & 1, 'b'))
                        message += str(format(pixels[x+(2*is_x), y+(2*is_y)][2] & 1, 'b'))

                    elif radio_text == "GBR":
                        message += str(format(pixels[x, y][1] & 1, 'b'))
                        message += str(format(pixels[x+(1*is_x), y+(1*is_y)][2] & 1, 'b'))
                        message += str(format(pixels[x+(2*is_x), y+(2*is_y)][0] & 1, 'b'))

                    elif radio_text == "BRG":
                        message += str(format(pixels[x, y][2] & 1, 'b'))
                        message += str(format(pixels[x+(1*is_x), y+(1*is_y)][0] & 1, 'b'))
                        message += str(format(pixels[x+(2*is_x), y+(2*is_y)][1] & 1, 'b'))

                    elif radio_text == "BGR":
                        message += str(format(pixels[x, y][2] & 1, 'b'))
                        message += str(format(pixels[x+(1*is_x), y+(1*is_y)][1] & 1, 'b'))
                        message += str(format(pixels[x+(2*is_x), y+(2*is_y)][0] & 1, 'b'))

                output = ''.join(chr(int(message[i:i+8], 2)) for i in range(0, len(message), 8))
                logic.writeOutput(window, output)
            except IsADirectoryError:
                logic.writeOutput(window, f"'{path}' is a directory, expecting image file.")
            except FileNotFoundError:
                logic.writeOutput(window, f"File '{path}' was not found on this computer.")
            except:
                logic.writeOutput(window, "Something went wrong.")

    def writeHidden(window, path, radio_text, pattern_text, order_text, length, text):
        pass
