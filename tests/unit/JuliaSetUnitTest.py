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

import unittest
import math
from Fractals import JuliaSet

class JuliaSetUnitTest(unittest.TestCase):
    def test_calc_point_0_0(self):
        juliaset = JuliaSet.JuliaSet(complex(0, 0))
        
        # length = 0
        val = juliaset.calcPoint(complex(0.0, 0.0), 101)
        self.assertEqual(val, 100)
        
        # 0 < length < 1
        val = juliaset.calcPoint(complex(0.5, 0.3), 101)
        self.assertEqual(val, 100)
        
        # length = 1
        val = juliaset.calcPoint(complex(1/math.sqrt(2), 1/math.sqrt(2)), 501)
        self.assertEqual(val, 100)
        val = juliaset.calcPoint(complex(0.0, 1.0), 101)
        self.assertEqual(val, 100)
        val = juliaset.calcPoint(complex(1.0, 0.0), 101)
        self.assertEqual(val, 100)
        # length > 1
        val = juliaset.calcPoint(complex(1.0, 1.0), 101)
        self.assertEqual(val, 0)
    
    def test_calc_point_0_1(self):
        juliaset = JuliaSet.JuliaSet(complex(0, 1))
        
        # length = 0
        val = juliaset.calcPoint(complex(0.0, 0.0), 101)
        self.assertEqual(val, 100)
        
        # 0 < length < 1
        val = juliaset.calcPoint(complex(0.5, 0.3), 101)
        self.assertEqual(val, 100)
        
        # length = 1
        val = juliaset.calcPoint(complex(1/math.sqrt(2), 1/math.sqrt(2)), 101)
        self.assertEqual(val, 100)
        val = juliaset.calcPoint(complex(0.0, 1.0), 501)
        self.assertEqual(val, 100)
        val = juliaset.calcPoint(complex(1.0, 0.0), 501)
        self.assertEqual(val, 100)
        # length > 1
        val = juliaset.calcPoint(complex(1.0, 1.0), 501)
        self.assertEqual(val, 0)
        
if __name__ == '__main__':
    unittest.main()