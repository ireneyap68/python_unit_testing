import unittest
import calc

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(100, 1), 101)
        self.assertEqual(calc.add(-88, 88), 0)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5), 5)
        self.assertEqual(calc.subtract(100, 1), 99)
        self.assertEqual(calc.subtract(-88, 88), -176)

    def test_divide(self):
        self.assertEqual(calc.divide(10,5), 2)
        self.assertEqual(calc.divide(100, 1), 100)
        self.assertEqual(calc.divide(-88, 88), -1)

        # self.assertRaises(ValueError, calc.divide, 10, 0)
        # either one method to test valueerror
        with self.assertRaises(ValueError):
            calc.divide(10,0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5), 50)
        self.assertEqual(calc.multiply(100, 1), 100)
        self.assertEqual(calc.multiply(-88, 88), -7744)

if __name__ == '__main__':
    unittest.main()
