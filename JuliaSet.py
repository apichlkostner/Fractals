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

from PyQt5.QtGui import QColor, QImage
import threading
import numpy as np
import multiprocessing
from numpy import sqrt

class JuliaSet():
    juliaImage = None
    rawData = None
    
    R = 0
    C = complex(0, 0)
    StartPhys = complex(0, 0)
    EndPhys   = complex(0, 0)
    ImageSize = (0, 0)
    
    def __init__(self, C):
        self.C = C
        self.R = (1 + sqrt(1 + 4 * abs(C))) / 2
        
    
    def calc(self):
        deltaPix = 500
        self.juliaImage = None
        self.rawData = np.empty([deltaPix, deltaPix])
        deltaX = 4
        deltaY = 4
        x0 = -2.0
        y0 = -2.0
        y1 = y0 + deltaY
        numCores = multiprocessing.cpu_count()
        print("Number of cores: %d", numCores)
        deltaCoreX = deltaX / numCores
        deltaCorePix = int(deltaPix / numCores)
        threads = []
        
        for c in range(numCores):
            start = complex(x0 + c * deltaCoreX, y0)
            end   = complex(x0 + (c + 1) * deltaCoreX, y1)
            startPix = (c * deltaCorePix, 0)
            endPix   = ((c + 1) * deltaCorePix, deltaPix)
            print("Starting thread for core %d" % c)
            print("Physical range (%d, %d), (%d, %d)" % (start.real, start.imag, end.real, end.imag))
            print("Pixel range (%d, %d), (%d, %d)" % (startPix[0], startPix[1], endPix[0], endPix[1]))
            t = threading.Thread(target=self.calcPart, args=(start, end, startPix, endPix))            
            threads.append(t)
            t.start()
            
        for t in threads:
            t.join()

    def calcPart(self, startPos, endPos, startPix, endPix):
        delta = endPos - startPos
        deltaPix = (endPix[0] - startPix[0], endPix[1] - startPix[1])
        for pixH in range(startPix[0], endPix[0]):
            xf = startPos.real + delta.real / deltaPix[0] * (pixH - startPix[0])
            for pixV in range(startPix[1], endPix[1]):
                yf = endPos.imag - delta.imag / deltaPix[1] * pixV
                self.rawData[pixH][pixV] = self.calcPoint(xf, yf)

    def calcPoint(self, xf, yf):
        jmval = complex(xf, yf)
        for val in range(100):
            jmval = jmval * jmval + self.C
            if abs(jmval) > self.R:
                break
        return val

    def calcImagePart(self, startPix, endPix):
        print("Calculating image from (%d, %d) to (%d, %d)" % (startPix[0], startPix[1], endPix[0], endPix[1]))
        for h in range(startPix[0], endPix[0]):
            for v in range(startPix[1], endPix[1]):
                val = self.rawData[h][v]
                #q = min(val * 7, 255)
                r = (val * 20) % 255
                g = (val * 40) % 255
                b = (val * 60) % 255
                self.juliaImage.setPixelColor(h, v, QColor(r, g, b))
                
    def getImage(self):
        if not self.juliaImage:
            s = self.rawData.shape
            self.juliaImage = QImage(s[0], s[1], QImage.Format_RGB32)
            numCores = multiprocessing.cpu_count()
            
            deltaCorePix = int(s[0] / numCores)
            threads = []
            
            for c in range(numCores):                
                startPix = (c * deltaCorePix, 0)
                endPix   = ((c + 1) * deltaCorePix, s[1])
                t = threading.Thread(target=self.calcImagePart, args=(startPix, endPix))            
                threads.append(t)
                t.start()
                
            for t in threads:
                t.join()
            
        return self.juliaImage
