import unittest

from ObjC2RubyMotion import CodeConverter

class ObjcToRubyMotion(unittest.TestCase):
    def setUp(self):
        pass

    def test_replace_nsstring(self):
        source   = 'NSDictionary *updatedLatte = [responseObject objectForKey:@"latte"];'
        expected = 'NSDictionary *updatedLatte = [responseObject objectForKey:"latte"];'
        self.assertEqual(CodeConverter(source).replace_nsstring(), expected)

    def test_convert_square_brackets_expression(self):
        source   = '[self notifyCreated];'
        expected = 'self.notifyCreated;'
        self.assertEqual(CodeConverter(source).convert_square_brackets_expression(), expected)

    def test_convert_square_brackets_expression_with_args(self):
        source   = '[self updateFromJSON:updatedLatte];'
        expected = 'self.updateFromJSON(updatedLatte);'
        self.assertEqual(CodeConverter(source).convert_square_brackets_expression(), expected)

    def test_convert_square_brackets_expression_with_multiple_args(self):
        source   = '[[[UITabBarItem alloc] initWithTabBarSystemItem:UITabBarSystemItemBookmarks tag:0] autorelease];'
        expected = 'UITabBarItem.alloc.initWithTabBarSystemItem(UITabBarSystemItemBookmarks,tag:0).autorelease;'
        self.assertEqual(CodeConverter(source).convert_square_brackets_expression(), expected)
