""" Test functions for linalg module
"""

from numpy.testing import *
set_package_path()
from numpy import linalg, arange, float64, array
restore_path()

rlevel = 1

class TestRegression(NumpyTestCase):
    def test_eig_build(self, level = rlevel):
        """Ticket #652"""
        rva = [1.03221168e+02 +0.j, 
               -1.91843603e+01 +0.j,
               -6.04004526e-01+15.84422474j, 
               -6.04004526e-01-15.84422474j,
               -1.13692929e+01 +0.j,
               -6.57612485e-01+10.41755503j,
               -6.57612485e-01-10.41755503j,
               1.82126812e+01 +0.j,
               1.06011014e+01 +0.j ,
               7.80732773e+00 +0.j ,
               -7.65390898e-01 +0.j,
               1.51971555e-15 +0.j ,
               -1.51308713e-15 +0.j]        
        a = arange(13*13, dtype = float64)
        a.shape = (13,13)
        a = a%17
        va, ve = linalg.eig(a)
        assert_array_almost_equal(va, rva)

    def test_eigh_build(self, level = rlevel):
        """Ticket 662."""
        rvals = [68.60568999, 89.57756725, 106.67185574]

        cov = array([[ 77.70273908,   3.51489954,  15.64602427],
                     [3.51489954,  88.97013878,  -1.07431931],
                     [15.64602427,  -1.07431931,  98.18223512]])
         
        vals, vecs = linalg.eigh(cov)
        assert_array_almost_equal(vals, rvals)

if __name__ == '__main__':
    NumpyTest().run()
