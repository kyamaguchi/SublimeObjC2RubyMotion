import sublime
import sublime_plugin
import os
import unittest
import StringIO
import sys

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.append(os.path.join(PROJECT_ROOT, "tests"))

g_executing_test_suite = None

test_suites = {
    'all': 'all_test',
    'basic': 'test_basic',
    'convert': 'test_replace'
}


def print_to_view(view, obtain_content):
    edit = view.begin_edit()
    view.insert(edit, 0, obtain_content())
    view.end_edit(edit)
    view.set_scratch(True)
    view.set_name('unittest results')

    return view

class ShowObjcToRubyMotionTestsSuites(sublime_plugin.WindowCommand):

    def run(self):
        self.window.show_quick_panel(
            sorted(test_suites.keys()),
            self.run_suite
        )

    def run_suite(self, index):
        global g_executing_test_suite

        suite_name = sorted(test_suites.keys())[index]
        g_executing_test_suite = suite_name
        command_to_run = 'objc_to_ruby_motion_tests'

        self.window.run_command(
            command_to_run,
            dict(suite_name=suite_name)
        )

class ObjcToRubyMotionTestsCommand(sublime_plugin.WindowCommand):

    def run(self, suite_name):
        bucket = StringIO.StringIO()
        if suite_name == 'all':
            suite_list = [unittest.defaultTestLoader.loadTestsFromName(str) for str in test_suites.values()]
            suite = unittest.TestSuite(suite_list)
        else:
            file_name = test_suites[suite_name]
            suite = unittest.defaultTestLoader.loadTestsFromName(file_name)
        unittest.TextTestRunner(stream=bucket, verbosity=1).run(suite)

        print_to_view(self.window.new_file(), bucket.getvalue)
