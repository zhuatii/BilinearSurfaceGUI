# Uses the class from the  form1.py
from form1 import Ui_MainWindow
from PyQt5.QtWidgets import QLabel

from matplotlib.backends.qt_compat import QtCore, QtWidgets

from PyQt5.QtWidgets import QLabel,QLineEdit
if QtCore.qVersion() >= "5.":
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

from matplotlib.figure import Figure

import sys
import numpy as np


class PlotCurveAndSurface(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.widget1 = QtWidgets.QWidget()
        self.ui.widget1.setGeometry(200, 200, 400, 400)
        self.setCentralWidget(self.ui.widget1)
       
        layout = QtWidgets.QVBoxLayout(self.ui.widget1)

        self.static_canvas_surf = FigureCanvas(Figure(figsize=(4, 3)))
        self.static_canvas_curv = FigureCanvas(Figure(figsize=(4, 3)))
        self.label1 = QLabel('Surface Plot', self)
        self.label1.move(25, 60)
        layout.addWidget(self.static_canvas_surf)
        self.displaybox1 = QLineEdit()
        layout.addWidget(self.displaybox1)
        layout.addWidget(self.ui.PlotBilinearSurface1)
        layout.addWidget(self.ui.PlotBilinearSurface2)
        self.label2 = QLabel('Curvature Plot', self)
        self.label2.move(25, 500)
        layout.addWidget(self.static_canvas_curv)
        self.displaybox2 = QLineEdit()
        layout.addWidget(self.displaybox2)
        layout.addWidget(self.ui.PlotGaussianCurve)
        layout.addWidget(self.ui.PlotMeanCurve)
        self.addToolBar(NavigationToolbar(self.static_canvas_surf, self))
        self.addToolBar(NavigationToolbar(self.static_canvas_curv, self))

        self._static_ax_surf = self.static_canvas_surf.figure.subplots()
        self._static_ax_curv = self.static_canvas_curv.figure.subplots()
        
        self.ui.PlotBilinearSurface1.toggled.connect(self.PlotBilinearSurface1)
        self.ui.PlotBilinearSurface2.toggled.connect(self.PlotBilinearSurface2)
        self.ui.PlotGaussianCurve.clicked.connect(self.PlotGaussianCurve)
        self.ui.PlotMeanCurve.clicked.connect(self.PlotMeanCurve)
    
    
    def PlotBilinearSurface1(self):
        global i
        print('Plotting Surface 1')
        i=1
        self.displaybox1.setText("Hyperbolic Paraboloid")
        
        self._static_ax_surf.axes.cla()
        self._static_ax_surf = self.static_canvas_surf.figure.add_subplot(111, projection = '3d')
        
        x = np.linspace(-6,6,30) #X coordinates
        y = np.linspace(-6,6,30) #Y coordinates
        
        X,Y=np.meshgrid(x,y) #Forming MeshGrid
        # meshgrid makes a retangular grid out of two 1-D arrays. 
        Z = self.f(X, Y,0,i) 
        self._static_ax_surf.plot_surface(X, Y, Z) 
        self.static_canvas_surf.draw_idle()       
    
    
    def PlotBilinearSurface2(self):
        global i
        print('Plotting Surface 2')
        i=2
        self.displaybox1.setText("")
        
        self._static_ax_surf.axes.cla()
        self._static_ax_surf = self.static_canvas_surf.figure.add_subplot(111, projection = '3d')
        
        u = np.linspace(0,1,30) #X coordinates
        v = np.linspace(0,1,30) #Y coordinates
        
        U,V=np.meshgrid(u,v) #Forming MeshGrid
        # meshgrid makes a retangular grid out of two 1-D arrays. 
        a = self.readData(2)

        X = a[0]*(1-U)*(1-V)+ a[3]*(U)*(1-V)+ a[6]*(1-U)*V + a[9]*U*V
        Y = a[1]*(1-U)*(1-V)+ a[4]*(U)*(1-V)+ a[7]*(1-U)*V + a[10]*U*V
        Z = a[2]*(1-U)*(1-V)+ a[5]*(U)*(1-V)+ a[8]*(1-U)*V + a[11]*U*V
        self._static_ax_surf.plot_surface(X,Y,Z) 
        self.static_canvas_surf.draw_idle()    
    
    def f(self,x,y,n,j): 
        
        a = self.readData(j)
        
        if n == 0:
            return a[0]+ a[1]*x + a[2]*y + a[3]*x*y # Z - coordinates
                    
        else:
            E = 1 + (a[1] + a[3]*y)**2
            F = (a[1]+a[3]*y)*(a[2]+a[3]*x)
            G = 1 + (a[2]+a[3]*x)**2
            M = a[3]*y
            
            if n == 2:
                return ((-1*M**2)/(E*G-F**2)) # gaussian curvature using first and second fundamental forms
            elif n == 3:  
                return (-1*F*M/(E*G-F**2)) # mean curvature simplified

            
    def readData(self,j): # reads file and solves for coefficients of bilinear surface polynomial
            if j==1:
                f = open('InputData1.txt','r+')
            else:
                f = open('InputData2.txt','r+')
                f.seek(0)
                data = f.read().split()
                data = [int(data[i]) for i in range(len(data))]
                return data
            f.seek(0)
            data = f.read().split()
            xi = [int(data[0]),int(data[4])]
            yi = [int(data[1]),int(data[3])]
            col = [int(data[i]) for i in range(8,12)]
            A = np.array([[1,xi[0],yi[0],xi[0]*yi[0]], [1,xi[0],yi[1],xi[0]*yi[1]], [1,xi[1],yi[0],xi[1]*yi[0]], [1,xi[1],yi[1],xi[1]*yi[0]]])
            b = np.array(col)
            a = np.linalg.solve(A, b)
            return a
    
    
    def PlotGaussianCurve(self):
        global i
        print('Plotting Gaussian Curvature for surface {}'.format(i))
        self.displaybox2.setText("Gaussian Curvature of Surface {}".format(i))
        self._static_ax_curv.axes.cla()
        self._static_ax_curv = self.static_canvas_curv.figure.add_subplot(111, projection = '3d')
                
        x = np.linspace(-6,6,30) #X coordinates
        y = np.linspace(-6,6,30) #Y coordinates
        
        X,Y=np.meshgrid(x,y) #Forming MeshGrid
        # meshgrid makes a retangular grid out of two 1-D arrays. 
        Z = self.f(X, Y,2,i) 
     
        self._static_ax_curv.plot_wireframe(X, Y, Z) 
        self.static_canvas_curv.draw_idle()
     
    
    def PlotMeanCurve(self):
        global i
        print('Plotting Mean Curvature for surface {}'.format(i))
        self.displaybox2.setText("Mean Curvature of Surface {}".format(i))
        self._static_ax_curv.axes.cla()
        self._static_ax_curv = self.static_canvas_curv.figure.add_subplot(111, projection = '3d')
        
        x = np.linspace(-6,6,30) #X coordinates
        y = np.linspace(-6,6,30) #Y coordinates
        
        X,Y=np.meshgrid(x,y) #Forming MeshGrid
        # meshgrid makes a retangular grid out of two 1-D arrays. 
        Z = self.f(X, Y,3,i) 
     
        self._static_ax_curv.plot_wireframe(X, Y, Z) 
        self.static_canvas_curv.draw_idle()
            
if __name__ == '__main__':
    
    app = QtWidgets.QApplication([])
    win = PlotCurveAndSurface()
    win.show()
    win.activateWindow()
    win.raise_()
    sys.exit(app.exec_())
        
