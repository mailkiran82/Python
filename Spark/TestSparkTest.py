#!python3 TestSparkTest.py
import unittest
import SparkTest


class TestSparkTest1(unittest.TestCase):
    def test_getCount(self):
        res = SparkTest.getCount()
        self.assertEqual(res,6)


if __name__ == '__main__':
    unittest.main()
