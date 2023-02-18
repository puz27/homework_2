from utils import arrs
import unittest


class Test(unittest.TestCase):
    def test_get_1(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)


    def test_get_2(self):
        with self.assertRaises(IndexError):
            assert arrs.get([], 0, "test") == "test"


    def test_slice_1(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])

    def test_slice_2(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
