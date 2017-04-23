#!/usr/bin/python3

# Copyright (C) 2017  Arthur Pichlkostner
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QPushButton
from PyQt5.QtGui import QColor, QPixmap, QImage

import JuliaSet

class Example(QWidget):
    pixmap = None
    myImage = None
    lbl = None
    
    def __init__(self):
        super().__init__()        
        self.initUI()
        
        
    def initUI(self):
        global pixmap, lbl 
        hbox = QHBoxLayout(self)
        
        okButton = QPushButton("OK")

        hbox.addWidget(okButton)
        
        lbl = QLabel(self)
        
        jm = JuliaSet.JuliaSet()
        jm.calc()
        juliaImage = jm.getImage()
        
        lbl.setPixmap(QPixmap(juliaImage))   

        hbox.addWidget(lbl)
        self.setLayout(hbox)
        
        self.setWindowTitle('Julia set')
        self.show()        
    
    def resizeEvent(self, *args, **kwargs):
        #pixmap_scaled = pixmap.scaledToWidth(self.width()-200)
        #lbl.setPixmap(pixmap_scaled)
        return QWidget.resizeEvent(self, *args, **kwargs)
    
    def resize(self, *args, **kwargs):
        ret = QWidget.resize(self, *args, **kwargs)
        pixmap_scaled = pixmap.scaledToWidth(self.width())
        lbl.setPixmap(pixmap_scaled)
        
        return ret 
                
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
