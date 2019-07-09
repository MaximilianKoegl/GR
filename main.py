from numpy import *
from pylab import *
from PyQt5 import  QtGui, QtCore, QtWidgets
from QDrawWidget import *
from ProjectiveTransformation import ProjectiveTransformation as pt
import pyqtgraph as pg
import recognizer
import template
import wiimote
import sys


class DrawingRecognizer(QtWidgets.QWidget):

    def __init__(self, draw_widget, btAddr):
        super(DrawingRecognizer, self).__init__()
        self.draw_widget = draw_widget
        self.connectingWiimote(btAddr)
        self.initUI()
        self.recognition = recognizer.Recognizer()
        self.setSavedTemplates()
        self.gameInterface()

        # just showing point on drawable
        transformation = pt()
        A = 450, 690
        B = 500, 300
        C = 950, 300
        D = 900, 700
        scoords = [A, B, C, D]
        point = transformation.getActualCoordinates(scoords)
        point = (point[0], 800-point[1])
        draw_widget.points = ([point])

    def connectingWiimote(self, btAddr):
        addr = btAddr
        name = None
        self.wm = wiimote.connect(addr, name)

    def setSavedTemplates(self):
        for i in template.templates:
            self.recognition.addTemplate(i)

    def gameInterface(self):
        while True:
            QtGui.QGuiApplication.processEvents()
            if self.wm.buttons["A"]:
                print(self.wm.ir.get_state())
                print("A")
            time.sleep(0.1)

    def recognition(self):
        self.predicted_label.setText("Compiling..")
        QtGui.QGuiApplication.processEvents()

        points = self.draw_widget.points
        if len(points) > 0:
           
            sample = self.recognition.recognize(points)[0]

            if sample is None:
                text = "~None~"
            else:
                text = sample.name
        else:
            text = "~None~"
        
        self.predicted_label.setText(text)

    def training(self):
        name = self.training_name_input.text()
        text = "Trained.."

        for x in self.recognition.templates:
            if x.name == name:
                text = "Already trained.."
                break
          
        points = self.draw_widget.points
       
        temp = template.Template(name, points)
        self.recognition.addTemplate(temp)
        self.trained_label.setText(text)
    
    def textChanged(self):
        self.trained_label.setText("")

        
    def initUI(self):
        layout = QtGui.QGridLayout()

        training_label = QtWidgets.QLabel("Set Name for training Gesture: ")
        self.training_name_input = QtWidgets.QLineEdit("")
        training_button = QtWidgets.QPushButton("Training")
        self.trained_label = QtWidgets.QLabel("")
        prediction_button = QtWidgets.QPushButton("Prediction")
        prediction_label = QtWidgets.QLabel("Predicted: ")
        self.predicted_label = QtWidgets.QLabel("~None~")

        prediction_button.clicked.connect(self.recognition)
        training_button.clicked.connect(self.training)
        self.training_name_input.textChanged.connect(self.textChanged)

        layout.addWidget(training_label)
        layout.addWidget(self.training_name_input)
        layout.addWidget(training_button)
        layout.addWidget(self.trained_label)
        layout.addWidget(prediction_button)
        layout.addWidget(self.predicted_label)
        self.setLayout(layout)
        self.setGeometry(810, 90, 200, 200)
        self.show()

def main():
    app = QtGui.QApplication([])
    win = QtGui.QMainWindow()
    win.setWindowTitle("AnalyzeWiimote")
    draw_widget = QDrawWidget()
    drawing_recognizer = DrawingRecognizer(draw_widget, sys.argv[1])

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
   