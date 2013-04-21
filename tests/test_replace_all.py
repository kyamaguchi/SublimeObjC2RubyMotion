import unittest, os, sys
from custom_test_case import CustomTestCase

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.append(os.path.join(PROJECT_ROOT, ".."))

from CodeConverter import CodeConverter

class TestReplaceAll(unittest.TestCase, CustomTestCase):

    # All replacement
    def test_replace_objc(self):
        source   = 'UIWindow* aWindow = [[[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]] autorelease];'
        expected = 'aWindow = UIWindow.alloc.initWithFrame(UIScreen.mainScreen.bounds)'
        self.assertSentence(CodeConverter(source).result(), expected)

    def test_block_with_two_args_in_one_line(self):
        source   = """[aSet enumerateObjectsUsingBlock:^(id obj, BOOL *stop){ obj = nil; } ];"""
        expected = """aSet.enumerateObjectsUsingBlock(->|obj,stop|{ obj = nil } )"""
        self.assertSentence(CodeConverter(source).result(), expected)

if __name__ == '__main__':
    unittest.main()
