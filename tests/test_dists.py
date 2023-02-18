from utils import dicts
import unittest


class Test(unittest.TestCase):
    def test_dicts(self):
        self.assertEqual(dicts.get_val({1: "first", 2: "second", 3: "third"}, 2), "second")


    def test_dicts_2(self):
        self.assertEqual(dicts.get_val({}, 999), {})


    def test_dicts_3(self):
        self.assertEqual(dicts.get_val({1: "first", 2: "second", 3: "third"}, 999), "git")