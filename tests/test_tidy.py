import unittest, os, sys
from custom_test_case import CustomTestCase

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.append(os.path.join(PROJECT_ROOT, ".."))

from CodeConverter import CodeConverter

class TestTidy(unittest.TestCase, CustomTestCase):

    def test_tidy_args(self):
        source   = """UITabBarItem.alloc.initWithTabBarSystemItem(UITabBarSystemItemBookmarks,tag:0)"""
        expected = """UITabBarItem.alloc.initWithTabBarSystemItem(UITabBarSystemItemBookmarks, tag:0)"""
        self.assertSentence(CodeConverter(source).tidy_up().s, expected)

if __name__ == '__main__':
    unittest.main()
