from PyQt5.QtWidgets import QApplication,QPushButton, QLabel, QMainWindow

app = QApplication([])

window = QMainWindow()
#cara2
label = QLabel(window)
label.setText("Label1 1")
label.move(200,0)

#cara1
button = QPushButton("MyButton",window)

window.show()
app.exec_()