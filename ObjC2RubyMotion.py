import sublime, sublime_plugin, sys

if sys.version_info >= (3, 0):
    from .CodeConverter import CodeConverter
else:
    from CodeConverter import CodeConverter

class ObjcToRubyMotionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                line = self.view.line(region)
                self.replace_objc(edit, line)
            else:
                self.replace_objc(edit, region)

    def replace_objc(self, edit, region):
        # Get the selected text
        s = self.view.substr(region)

        # Replace the selection with transformed text
        self.view.replace(edit, region, CodeConverter(s).result())
