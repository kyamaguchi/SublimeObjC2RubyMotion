import sublime, sublime_plugin, re

class CodeConverter(object):
    def __init__(self, s):
        self.s = s

    def replace_nsstring(self):
        return re.sub(r'@("(?:[^\\"]|\\.)*")', r'\1', self.s)

    def convert_square_brackets_expression(self):
        max_attempt = 10 # Avoid infinite loops
        attempt_count = 0
        square_pattern = re.compile(r'\[([^\[\]]+?)\s+([^\[\]]+?)\]')
        while True:
            attempt_count += 1
            m = re.search(square_pattern, self.s)
            if attempt_count > max_attempt :
                break
            elif m :
                self.s = re.sub(square_pattern, ruby_style_code, self.s)
            else :
                break
        return self.s

    def convert_args(matchobj):
        # Consider args with colon followed by spaces
        following_args = re.sub(r'([^:]+)(\s+)', r'\1,', matchobj.group(2))
        # Clear extra spaces
        following_args = re.sub(r'\s+', '', following_args)
        return "%s(%s)" % (matchobj.group(1), following_args)

    def ruby_style_code(matchobj):
        msg = re.sub(r'([^:]+)\:\s*(.+)', convert_args, matchobj.group(2))
        return "%s.%s" % (matchobj.group(1), msg)

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

        s = CodeConverter(s).replace_nsstring()
        s = CodeConverter(s).convert_square_brackets_expression()

        # Replace the selection with transformed text
        self.view.replace(edit, region, s)
