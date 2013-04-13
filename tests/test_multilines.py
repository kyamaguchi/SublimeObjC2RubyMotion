import unittest
import os, sys

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.append(os.path.join(PROJECT_ROOT, ".."))

from CodeConverter import CodeConverter

class TestMultilines(unittest.TestCase):
    def setUp(self):
        pass

    def test_multilines_to_one_line(self):
        source   = """first_line;
                      second_line
                      third_line"""
        expected = """first_line;
                      second_line third_line"""
        self.assertEqual(CodeConverter(source).multilines_to_one_line().s, expected)

    def test_multilines_to_one_line_with_args(self):
        source   = """UIAlertView* alert = [[[UIAlertView alloc] initWithTitle:@"Warning"
                                                                       message:@"too many alerts"
                                                                      delegate:nil"""
        expected = 'UIAlertView* alert = [[[UIAlertView alloc] initWithTitle:@"Warning" message:@"too many alerts" delegate:nil'
        self.assertEqual(CodeConverter(source).multilines_to_one_line().s, expected)

    def test_multilines_to_one_line_for_trailing_white_space(self):
        source   = """first_line;
                      second_line   """
        expected = """first_line;
                      second_line"""
        self.assertEqual(CodeConverter(source).multilines_to_one_line().s, expected)

    def test_multilines_to_one_line_for_blank_line(self):
        source   = """first_line;

                      second_line"""
        expected = """first_line;

                      second_line"""
        self.assertEqual(CodeConverter(source).multilines_to_one_line().s, expected)

    def test_multiline_with_braces(self):
        source   = """    if (self) {
        [self addMainLabel];
        [self addSubLabel];
        [self setupBackground];
    }
"""
        expected = """    if (self) {
        self.addMainLabel
        self.addSubLabel
        self.setupBackground
    }
"""
        result = CodeConverter(source).result()
        self.assertEqual(result, expected)

    def test_multiline_expression(self):
        source   = """UIAlertView* alert = [[[UIAlertView alloc] initWithTitle:@"Warning"
                                                                       message:@"too many alerts"
                                                                      delegate:nil
                                                             cancelButtonTitle:@"OK"
                                                             otherButtonTitles:nil] autorelease];
                      [alert show]"""
        expected = """alert = UIAlertView.alloc.initWithTitle("Warning",message:"too many alerts",delegate:nil,cancelButtonTitle:"OK",otherButtonTitles:nil)
                      alert.show"""
        result = CodeConverter(source).result()
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
