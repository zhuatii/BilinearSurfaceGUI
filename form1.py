from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(250, 30, 531, 491))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        
        self.widget1.setSizePolicy(sizePolicy)
        self.widget1.setAutoFillBackground(True)
        self.widget1.setObjectName("widget1")
                
        self.PlotBilinearSurface1 = QtWidgets.QRadioButton(self.centralwidget)
        self.PlotBilinearSurface1.setGeometry(QtCore.QRect(30, 80, 161, 32))
        self.PlotBilinearSurface1.setObjectName("PlotBilinearSurface1")
        
        self.PlotBilinearSurface2 = QtWidgets.QRadioButton(self.centralwidget)
        self.PlotBilinearSurface2.setGeometry(QtCore.QRect(30, 80, 161, 32))
        self.PlotBilinearSurface2.setObjectName("PlotBilinearSurface2")
        
        self.PlotGaussianCurve = QtWidgets.QPushButton(self.centralwidget)
        self.PlotGaussianCurve.setGeometry(QtCore.QRect(30, 40, 161, 32))
        self.PlotGaussianCurve.setObjectName("PlotGaussianCurve")
        
        self.PlotMeanCurve = QtWidgets.QPushButton(self.centralwidget)
        self.PlotMeanCurve.setGeometry(QtCore.QRect(30, 40, 161, 32))
        self.PlotMeanCurve.setObjectName("PlotMeanCurve")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        
    

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bilinear Surface"))
        self.PlotBilinearSurface1.setText(_translate("MainWindow", "Surface 1"))
        self.PlotBilinearSurface2.setText(_translate("MainWindow", "Surface 2"))
        self.PlotGaussianCurve.setText(_translate("MainWindow", "Gaussian curvature"))
        self.PlotMeanCurve.setText(_translate("MainWindow", "Mean curvature"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
