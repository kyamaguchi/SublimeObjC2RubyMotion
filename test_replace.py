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

    def test_remove_semicolon_at_the_end(self):
        source   = '[[[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]] autorelease];'
        expected = '[[[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]] autorelease]'
        self.assertEqual(CodeConverter(source).remove_semicolon_at_the_end(), expected)

    def test_remove_autorelease(self):
        source   = '[[[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]] autorelease]'
        expected = 'UIWindow.alloc.initWithFrame(UIScreen.mainScreen.bounds)'
        source = CodeConverter(source).convert_square_brackets_expression()
        source = CodeConverter(source).remove_autorelease()
        self.assertEqual(source, expected)

    # All replacement
    def test_replace_objc(self):
        source   = '[[[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]] autorelease];'
        expected = 'UIWindow.alloc.initWithFrame(UIScreen.mainScreen.bounds)'
        source = CodeConverter(source).replace_nsstring()
        source = CodeConverter(source).convert_square_brackets_expression()
        source = CodeConverter(source).remove_semicolon_at_the_end()
        source = CodeConverter(source).remove_autorelease()
        self.assertEqual(source, expected)
