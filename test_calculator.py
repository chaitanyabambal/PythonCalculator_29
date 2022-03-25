import calculator
import unittest


class TestClass(unittest.TestCase):

    def setUp(self):
        self.x = 34
        self.y = 30

    def tearDownClass(self):
        self.x = 0
        self.y = 0

    def test_Add(self):
        # act
        result = calculator.add(self.x, self.y)
        # assert
        self.assertEqual(result, self.x + self.y)

    def test_sub(self):
        result = calculator.sub(self.x, self.y)
        self.assertEqual(result, self.x - self.y)

    def test_mult(self):
        result = calculator.mult(self.x, self.y)
        self.assertEqual(result, self.x * self.y)

    def test_div(self):
        result = calculator.div(self.x, self.y)
        self.assertEqual(result, self.x / self.y)

    if __name__ == '__main__':
        unittest.main()
