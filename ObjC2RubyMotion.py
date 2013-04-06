import sublime, sublime_plugin, re

class CodeConverter(object):
    def __init__(self, s):
        self.s = s

    # Helpers
    def convert_args(self, matchobj):
        # Consider args with colon followed by spaces
        following_args = re.sub(r'([^:]+)(\s+)', r'\1,', matchobj.group(2))
        # Clear extra spaces
        following_args = re.sub(r'\s+', '', following_args)
        return "%s(%s)" % (matchobj.group(1), following_args)

    def ruby_style_code(self, matchobj):
        msg = re.sub(r'([^:]+)\:\s*(.+)', self.convert_args, matchobj.group(2))
        return "%s.%s" % (matchobj.group(1), msg)

    # Conversions
    def replace_nsstring(self):
        self.s = re.sub(r'@("(?:[^\\"]|\\.)*")', r'\1', self.s)
        return self

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
                self.s = re.sub(square_pattern, self.ruby_style_code, self.s)
            else :
                break
        return self

    def remove_semicolon_at_the_end(self):
        self.s = re.sub(r';', '', self.s)
        return self

    def remove_autorelease(self):
        self.s = re.sub(r'\.autorelease$', '', self.s)
        return self

    def remove_type_declaration(self):
        self.s = re.sub(r'^(\s*)[a-zA-Z_0-9]+\s*\*\s*([^=]+)=', r'\1\2=', self.s)
        return self

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

        obj = CodeConverter(s)
        obj.replace_nsstring()
        obj.convert_square_brackets_expression()
        obj.remove_semicolon_at_the_end()
        obj.remove_autorelease()

        obj.remove_type_declaration()

        # Replace the selection with transformed text
        self.view.replace(edit, region, obj.s)
