#!/usr/bin/python3

#    Fractal - calculation of fractals
#    Copyright (C) 2017 Arthur Pichlkostner
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QDoubleSpinBox
from PyQt5.QtGui import QColor, QPixmap, QImage
import time

import JuliaSet

class MainWindow(QWidget):
    myImage = None
    
    def __init__(self):
        super().__init__()        
        self.initUI()
        
        
    def initUI(self):
        hbox = QHBoxLayout(self)
        
        # userinterface
        interface_vbox = QVBoxLayout()        
        
        self.dsb_real = QDoubleSpinBox()
        self.dsb_real.setMinimum(-100)
        self.dsb_real.setMaximum(100)
        interface_vbox.addWidget(self.dsb_real)
        
        self.dsb_complex = QDoubleSpinBox()
        self.dsb_complex.setMinimum(-100)
        self.dsb_complex.setMaximum(100)
        self.dsb_complex.setValue(1.0)
        interface_vbox.addWidget(self.dsb_complex)
        
        calcButton = QPushButton("Calculate")
        interface_vbox.addWidget(calcButton)
        calcButton.clicked.connect(self.calcClicked)
        
        exitButton = QPushButton("Exit")
        interface_vbox.addWidget(exitButton)
        exitButton.clicked.connect(self.exitClicked)
                
        hbox.addLayout(interface_vbox)
        
        self.lbl = QLabel(self)
        emptyPixmap = QPixmap(500, 500)
        emptyPixmap.fill(QColor(100, 100, 100))
        self.lbl.setPixmap(emptyPixmap)
        #jm = JuliaSet.JuliaSet(complex(0.25, 0))
        #jm.calc()
        #juliaImage = jm.getImage()
        
        #lbl.setPixmap(QPixmap(juliaImage))   

        hbox.addWidget(self.lbl)
        self.setLayout(hbox)
        
        self.setWindowTitle('Julia set')
        self.show()
        self.calcClicked()
    
    def resizeEvent(self, *args, **kwargs):
        #pixmap_scaled = pixmap.scaledToWidth(self.width()-200)
        #lbl.setPixmap(pixmap_scaled)
        return QWidget.resizeEvent(self, *args, **kwargs)
    
    def resize(self, *args, **kwargs):
        ret = QWidget.resize(self, *args, **kwargs)
        pixmap_scaled = self.pixmap.scaledToWidth(self.width())
        self.lbl.setPixmap(pixmap_scaled)
        
        return ret 
    
    def calcClicked(self):
        val_real = self.dsb_real.value()
        val_complex = self.dsb_complex.value()
        self.jm = JuliaSet.JuliaSet(complex(val_real, val_complex))
        self.jm.calc()
        juliaImage = self.jm.getImage()        
        self.lbl.setPixmap(QPixmap(juliaImage)) 
        
    def exitClicked(self):
        quit()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
