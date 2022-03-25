import calculator
import unittest


class TestCalculator(unittest.TestCase):
    def test_Add(self):
        x = 10
        y = 20
        result = calculator.add(x, y)
        self.assertEqual(result, x + y)

    def test_sub(self):
        x = 10
        y = 20
        result = calculator.sub(x, y)
        self.assertEqual(result, x - y)

    def test_mult(self):
        x = 10
        y = 20
        result = calculator.mult(x, y)
        self.assertEqual(result, x * y)

    def test_div(self):
        x = 30
        y = 10
        result = calculator.div(x, y)
        self.assertEqual(result, x)

    if __name__ == '__main__':
        unittest.main()
