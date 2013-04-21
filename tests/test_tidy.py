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

    def test_tidy_args(self):
        source   = 'NSLog(@"test,string:")'
        expected = 'NSLog("test,string:")'
        self.assertSentence(CodeConverter(source).result(), expected)

    def test_tidy_args_with_block(self):
        source   = """UIView.animateWithDuration(0.2,animations:->{ view.alpha = 0.0 })"""
        expected = """UIView.animateWithDuration(0.2, animations: -> { view.alpha = 0.0 })"""
        self.assertSentence(CodeConverter(source).result(), expected)

    def test_tidy_block_with_one_args(self):
        source   = """[UIView animateWithDuration:0.2
                             animations:^{ view.alpha = 0.0; }
                             completion:^( BOOL finished ){ [view removeFromSuperview]; }];"""
        expected = """UIView.animateWithDuration(0.2, animations: -> { view.alpha = 0.0 }, completion: -> finished { view.removeFromSuperview })"""
        self.assertSentence(CodeConverter(source).result(), expected)

if __name__ == '__main__':
    unittest.main()
