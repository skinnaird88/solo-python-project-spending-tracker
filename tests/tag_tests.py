import unittest
from console import tag1, tag2

class TagTests(unittest.TestCase):
    def test_tag_name(self):
        self.assertEqual("groceries", tag1.name)

    def test_tag2_name(self):
        self.assertEqual("motor", tag2.name)
