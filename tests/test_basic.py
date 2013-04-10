import unittest
import os, sys

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.append(os.path.join(PROJECT_ROOT, ".."))

from CodeConverter import CodeConverter

class TestBasic(unittest.TestCase):
    def setUp(self):
        pass

    def test_initialize(self):
        self.assertEqual(CodeConverter('foo').s, 'foo')

if __name__ == '__main__':
    unittest.main()
