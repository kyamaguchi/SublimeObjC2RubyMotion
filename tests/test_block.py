import unittest
import os, sys

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.append(os.path.join(PROJECT_ROOT, ".."))

from CodeConverter import CodeConverter

class TestBlock(unittest.TestCase):

    def test_preserve_multilines_with_block_with_multilines(self):
        source   = """[aSet enumerateObjectsUsingBlock:^(id obj, BOOL *stop){
     NSLog(@"Object Found: %@", obj);
} ];"""
        expected = """[aSet enumerateObjectsUsingBlock:^(id obj, BOOL *stop){
     NSLog(@"Object Found: %@", obj);
} ];"""
        self.assertEqual(CodeConverter(source).multilines_to_one_line().s, expected)

    def test_multilines_with_one_line_block(self):
        source   = """[UIView animateWithDuration:0.2
                             animations:^{view.alpha = 0.0;}]"""
        expected = """[UIView animateWithDuration:0.2 animations:^{view.alpha = 0.0;}]"""
        self.assertEqual(CodeConverter(source).multilines_to_one_line().s, expected)

    def test_multilines_with_one_line_blocks(self):
        source   = """[UIView animateWithDuration:0.2
                             animations:^{view.alpha = 0.0;}
                             completion:^(BOOL finished){ [view removeFromSuperview]; }];"""
        expected = """[UIView animateWithDuration:0.2 animations:^{view.alpha = 0.0;} completion:^(BOOL finished){ [view removeFromSuperview]; }];"""
        self.assertEqual(CodeConverter(source).multilines_to_one_line().s, expected)

    def test_block_without_args(self):
        source   = """[UIView animateWithDuration:0.2
                             animations:^{view.alpha = 0.0;}]"""
        expected = """[UIView animateWithDuration:0.2 animations:->{view.alpha = 0.0;}]"""
        self.assertEqual(CodeConverter(source).multilines_to_one_line().convert_blocks().s, expected)

    def test_block_with_one_args(self):
        source   = """[UIView animateWithDuration:0.2
                             animations:^{view.alpha = 0.0;}
                             completion:^( BOOL finished ){ [view removeFromSuperview]; }];"""
        expected = """[UIView animateWithDuration:0.2 animations:->{view.alpha = 0.0;} completion:->finished{ [view removeFromSuperview]; }];"""
        self.assertEqual(CodeConverter(source).multilines_to_one_line().convert_blocks().s, expected)

    def test_block_with_two_args(self):
        source   = """[aSet enumerateObjectsUsingBlock:^(id obj, BOOL *stop){
      NSLog(@"Object Found: %@", obj);
} ];"""
        expected = """[aSet enumerateObjectsUsingBlock:->|obj,stop|{
      NSLog(@"Object Found: %@", obj);
} ];"""
        self.assertEqual(CodeConverter(source).multilines_to_one_line().convert_blocks().s, expected)

if __name__ == '__main__':
    unittest.main()
