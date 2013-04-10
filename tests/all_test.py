import glob
import unittest
import os, sys

if __name__ == '__main__':
    PROJECT_ROOT = os.path.dirname(__file__)
    test_file_strings = glob.glob(os.path.join(PROJECT_ROOT, 'test_*.py'))
    module_strings = [os.path.splitext(os.path.basename(str))[0] for str in test_file_strings]
    suites = [unittest.defaultTestLoader.loadTestsFromName(str) for str in module_strings]
    testSuite = unittest.TestSuite(suites)
    text_runner = unittest.TextTestRunner().run(testSuite)
