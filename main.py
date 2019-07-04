from numpy import *
from pylab import *
from PyQt5 import  QtGui, QtCore, QtWidgets
from QDrawWidget import *
from ProjectiveTransformation import ProjectiveTransformation as pt
import pyqtgraph as pg

class DrawingRecognizer(QtWidgets.QWidget):

    def __init__(self, draw_widget):
        super(DrawingRecognizer, self).__init__()
        self.draw_widget = draw_widget
        self.initUI()

        transformation = pt()
        # just showing point on drawable
        A = 450, 690
        B = 500, 300
        C = 950, 300
        D = 900, 700
        scoords = [A, B, C, D]
        point = transformation.getActualCoordinates(scoords)
        point = (point[0], 800-point[1])
        print(point)
        draw_widget.points = ([point])
    

    def initUI(self):
        layout = QtGui.QGridLayout()

        training_label = QtWidgets.QLabel("Set Name for training Gesture: ")
        training_name_input = QtWidgets.QLineEdit("")
        training_button = QtWidgets.QPushButton("Training")
        prediction_button = QtWidgets.QPushButton("Prediction")
        prediction_label = QtWidgets.QLabel("Predicted: ")
        predicted_label = QtWidgets.QLabel("~None~")

        layout.addWidget(training_label)
        layout.addWidget(training_name_input)
        layout.addWidget(training_button)
        layout.addWidget(prediction_button)
        layout.addWidget(predicted_label)
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
   