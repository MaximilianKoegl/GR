from numpy import *
from pylab import *
from PyQt5 import  QtGui, QtCore, QtWidgets
import pyqtgraph as pg
from QDrawWidget import *

class DrawingRecognizer(QtWidgets.QWidget):

    def __init__(self, draw_widget):
        super(DrawingRecognizer, self).__init__()
        self.draw_widget = draw_widget
        self.initUI()
    

    def initUI(self):
        layout = QtGui.QGridLayout()

        training_button = QtWidgets.QPushButton("Training")
        prediction_button = QtWidgets.QPushButton("Prediction")
        prediction_label = QtWidgets.QLabel("Predicted: ")
        predicted_label = QtWidgets.QLabel("~None~")
        training_name_input = QtWidgets.QLineEdit("trained name")

        layout.addWidget(training_button, 0, 1)
        layout.addWidget(prediction_button, 1, 1)
        layout.addWidget(predicted_label, 2, 1)
        layout.addWidget(training_name_input, 3, 1)
        self.setLayout(layout)
        self.setGeometry(810, 90, 200, 200)
        self.show()

def main():
    app = QtGui.QApplication([])
    win = QtGui.QMainWindow()
    win.setWindowTitle("AnalyzeWiimote")
    draw_widget = QDrawWidget()
    drawing_recognizer = DrawingRecognizer(draw_widget)

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
   