import unittest
import sys

# import ObjC2RubyMotion
# ObjC2RubyMotion = reload(ObjC2RubyMotion)
from ObjC2RubyMotion import CodeConverter

class ObjcToRubyMotion(unittest.TestCase):
    def setUp(self):
        pass

    def test_initialize(self):
        self.assertEqual(CodeConverter('foo').s, 'foo')

    def test_replace_nsstring(self):
        source   = 'NSDictionary *updatedLatte = [responseObject objectForKey:@"latte"];'
        expected = 'NSDictionary *updatedLatte = [responseObject objectForKey:"latte"];'
        self.assertEqual(CodeConverter(source).replace_nsstring().s, expected)

    def test_convert_square_brackets_expression(self):
        source   = '[self notifyCreated];'
        expected = 'self.notifyCreated;'
        self.assertEqual(CodeConverter(source).convert_square_brackets_expression().s, expected)

    def test_convert_square_brackets_expression_with_args(self):
        source   = '[self updateFromJSON:updatedLatte];'
        expected = 'self.updateFromJSON(updatedLatte);'
        self.assertEqual(CodeConverter(source).convert_square_brackets_expression().s, expected)

    def test_convert_square_brackets_expression_with_multiple_args(self):
        source   = '[[[UITabBarItem alloc] initWithTabBarSystemItem:UITabBarSystemItemBookmarks tag:0] autorelease];'
        expected = 'UITabBarItem.alloc.initWithTabBarSystemItem(UITabBarSystemItemBookmarks,tag:0).autorelease;'
        self.assertEqual(CodeConverter(source).convert_square_brackets_expression().s, expected)

    def test_remove_semicolon_at_the_end(self):
        source   = '[[[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]] autorelease];'
        expected = '[[[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]] autorelease]'
        self.assertEqual(CodeConverter(source).remove_semicolon_at_the_end().s, expected)

    def test_remove_autorelease(self):
        source   = '[[[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]] autorelease]'
        expected = 'UIWindow.alloc.initWithFrame(UIScreen.mainScreen.bounds)'
        obj = CodeConverter(source).convert_square_brackets_expression()
        obj.remove_autorelease()
        self.assertEqual(obj.s, expected)

    def test_remove_type_declaration(self):
        source   = 'UIWindow* aWindow = [[[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]] autorelease]'
        expected = 'aWindow = [[[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]] autorelease]'
        self.assertEqual(CodeConverter(source).remove_type_declaration().s, expected)

    def test_remove_type_declaration_with_lead_spaces(self):
        source   = '    UIWindow* aWindow = [[[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]] autorelease]'
        expected = '    aWindow = [[[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]] autorelease]'
        self.assertEqual(CodeConverter(source).remove_type_declaration().s, expected)

    # All replacement
    def test_replace_objc(self):
        source   = 'UIWindow* aWindow = [[[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]] autorelease];'
        expected = 'aWindow = UIWindow.alloc.initWithFrame(UIScreen.mainScreen.bounds)'
        obj = CodeConverter(source).replace_nsstring()
        obj.convert_square_brackets_expression()
        obj.remove_semicolon_at_the_end()
        obj.remove_autorelease()
        obj.remove_type_declaration()
        self.assertEqual(obj.s, expected)
