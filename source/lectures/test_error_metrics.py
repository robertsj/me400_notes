import unittest
from math import sqrt

from error_metrics import mean_abs_error, rms_error, max_abs_error

class TestErrorMetrics(unittest.TestCase) :
    """The class name is TestErrorMetrics and should indicate in some way
       what is being tested."""
          
    def test_mean_abs_error(self) :
        e = [0.1, -0.2, 0.3]
        # assertAlmostEqual comparse two values (here, 
        # mean_abs_error(e) and 0.2) and ensures they are the same
        # out to 14 decimal places (i.e., 10^-14)
        self.assertAlmostEqual(mean_abs_error(e), 0.2, places=14)

    def test_rms_error(self) :
        e = [0.1, -0.2, 0.3]
        self.assertAlmostEqual(rms_error(e), sqrt(0.14), places=14)

    def test_max_abs_error(self) :
        e = [0.1, -0.2, 0.3]
        self.assertAlmostEqual(max_abs_error(e), 0.3, places=14)

if __name__ == '__main__':
    unittest.main()
