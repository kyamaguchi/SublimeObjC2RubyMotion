import unittest, os, sys
from custom_test_case import CustomTestCase

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.append(os.path.join(PROJECT_ROOT, ".."))

from CodeConverter import CodeConverter

class TestNumber(unittest.TestCase, CustomTestCase):

    def test_convert_float(self):
        source   = 'CGRect rect = CGRectMake(100.0f, 100.0f, 10.5f, 10.5f);'
        expected = 'CGRect rect = CGRectMake(100, 100, 10.5, 10.5);'
        self.assertSentence(CodeConverter(source).convert_float().s, expected)

if __name__ == '__main__':
    unittest.main()
