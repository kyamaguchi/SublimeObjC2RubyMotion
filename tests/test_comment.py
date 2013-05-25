import unittest, os, sys
from custom_test_case import CustomTestCase

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.append(os.path.join(PROJECT_ROOT, ".."))

from CodeConverter import CodeConverter

class TestComment(unittest.TestCase, CustomTestCase):

    def test_remove_line_comment(self):
        source   = """  // comment here
  [self foo];"""
        expected = '  [self foo];'
        self.assertSentence(CodeConverter(source).remove_comments().s, expected)

    def test_remove_line_comment_in_multilines(self):
        source   = """
  // comment here
  [self foo];

  // comment2 here
  [self bar];
"""
        expected = """
  [self foo];

  [self bar];
"""
        self.assertSentence(CodeConverter(source).remove_comments().s, expected)

    def test_remove_inline_comment(self):
        source   = '  [self foo];// comment here '
        expected = '  [self foo];'
        self.assertSentence(CodeConverter(source).remove_comments().s, expected)

    def test_dont_remove_url(self):
        source   = 'NSURL* url = [NSURL URLWithString:@"http://www.sublimetext.com/"];'
        expected = 'url = NSURL.URLWithString("http://www.sublimetext.com/")'
        self.assertSentence(CodeConverter(source).result(), expected)

    def test_remove_inline_comment_in_multilines(self):
        source   = """  [self foo];// comment here
  [self bar];// comment2 here"""
        expected = """  [self foo];
  [self bar];"""
        self.assertSentence(CodeConverter(source).remove_comments().s, expected)

if __name__ == '__main__':
    unittest.main()
