import unittest
import os, sys

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.append(os.path.join(PROJECT_ROOT, ".."))

from CodeConverter import CodeConverter

class TestBugfix(unittest.TestCase):

    # For Bugfix
    def test_string_including_spaces(self):
        source   = '[[UIAlertView alloc] initWithTitle:@"Warning" message:@"  too many alerts!  \"  "];'
        expected = 'UIAlertView.alloc.initWithTitle("Warning",message:"  too many alerts!  \"  ");'
        self.assertEqual(CodeConverter(source).replace_nsstring().convert_square_brackets_expression().s, expected)

if __name__ == '__main__':
    unittest.main()
