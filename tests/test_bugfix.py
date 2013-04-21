import unittest, os, sys
from custom_test_case import CustomTestCase

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.append(os.path.join(PROJECT_ROOT, ".."))

from CodeConverter import CodeConverter

class TestBugfix(unittest.TestCase, CustomTestCase):

    # For Bugfix
    def test_string_including_spaces(self):
        source   = '[[UIAlertView alloc] initWithTitle:@"Warning" message:@"  too many alerts!  \"  "];'
        expected = 'UIAlertView.alloc.initWithTitle("Warning",message:"  too many alerts!  \"  ");'
        self.assertSentence(CodeConverter(source).replace_nsstring().convert_square_brackets_expression().s, expected)

    def test_multiline_with_block_arg_wont_join_lines(self):
        source   = """[UIView animateWithDuration:0.2
                             animations:^{view.alpha = 0.0;}]
"""
        expected = """[UIView animateWithDuration:0.2 animations:^{view.alpha = 0.0;}]
"""
        self.assertSentence(CodeConverter(source).multilines_to_one_line().s, expected)

if __name__ == '__main__':
    unittest.main()
