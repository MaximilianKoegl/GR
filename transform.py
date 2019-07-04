from numpy import *
from pylab import *
from PyQt5 import  QtGui, QtCore, QtWidgets
import pyqtgraph as pg
from QDrawWidget import *


WIIMOTE_IR_CAM_WIDTH, WIIMOTE_IR_CAM_HEIGHT = 1024, 768 # the dimensions 
# Four IR markers indicating the corners of the display with which we interact

# needs some more pre-processing in practical usage
# sorting of points required 
# define which one is the top left corner, bottom left corner, ...

A = 450, 690
B = 500, 300
C = 950, 300
D = 900, 700
scoords = [A, B, C, D]


def step_one(scoords):

    # Step 1
    source_points_123 = matrix([[A[0], B[0], C[0]], 
                                [A[1], B[1], C[1]], 
                                [  1 ,   1 ,   1 ]])

    source_point_4 = [[D[0]],
                    [D[1]],
                    [ 1 ]]

    # solve the system of linear equations
    scale_to_source = solve(source_points_123, source_point_4)

    l, m, t = [float(x) for x in scale_to_source]


def step_two(A, B, C, l, m, t)
    # Step 2
    identity_to_source = matrix([[l * A[0], m * B[0], t * C[0]], 
                                [l * A[1], m * B[1], t* C[1]], 
                                [     l ,      m ,    t ]])

def step_three()

    # Step 3
    DESTINATION_SCREEN_WIDTH = 1280
    DESTINATION_SCREEN_HEIGHT = 720

    A2 = 0, DESTINATION_SCREEN_HEIGHT
    B2 = 0, 0
    C2 = DESTINATION_SCREEN_WIDTH, 0
    D2 = DESTINATION_SCREEN_WIDTH, DESTINATION_SCREEN_HEIGHT

    dcoords = [A2, B2, C2, D2]

    dest_points_123 = matrix([[A2[0], B2[0], C2[0]], 
                            [A2[1], B2[1], C2[1]], 
                            [  1 ,   1 ,   1 ]])
                
    dest_point_4 = matrix([[D2[0]],
                        [D2[1]],
                        [ 1 ]])
                
    scale_to_dest = solve(dest_points_123, dest_point_4)
    l,m,t = [float(x) for x in scale_to_dest]


    identity_to_dest = matrix([[l * A2[0], m * B2[0], t * C2[0]], 
                            [l * A2[1], m * B2[1], t * C2[1]], 
                            [      l ,       m ,      t ]])

    # invert matrix
    source_to_identity = inv(identity_to_source)

    # multiply B with invertex matrix A
    source_to_dest = identity_to_dest @ source_to_identity

    x, y, z = [float(w) for w in (source_to_dest @ matrix([[512],
                                                        [384],
                                                        [ 1 ]]))]
    x = x / z
    y = y / z

xlim(0, DESTINATION_SCREEN_WIDTH)
ylim(0, DESTINATION_SCREEN_HEIGHT)
scatter(*zip(*dcoords)) # repack points[] to axes[] for plotting
scatter([x],[y],c='r',marker='+') # center of the Wiimote sensor


if __name__ == '__main__':
    app = QtGui.QApplication([])
    win = QtGui.QMainWindow()
    win.setWindowTitle("AnalyzeWiimote")
    cw = QtGui.QWidget()
    win.setCentralWidget(cw)
    layout = QtGui.QGridLayout()
    cw.setLayout(layout)
    widget = QDrawWidget()
    layout.addWidget(widget)
    widget.points = [(x,800-y)]
    win.show()
    QtGui.QApplication.instance().exec()
