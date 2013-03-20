import sublime, sublime_plugin, re

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
        # NSString to String
        s = re.sub(r'@("(?:[^\\"]|\\.)*")', r'\1', s)
        # Convert square brackets expression
        max_attempt = 10 # Avoid infinite loops
        attempt_count = 0
        square_pattern = re.compile(r'\[([^\[\]]+?)\s+([^\[\]]+?)\]')
        while True:
            attempt_count += 1
            m = re.search(square_pattern, s)
            if attempt_count > max_attempt :
                break
            elif m :
                s = re.sub(square_pattern, ruby_style_code, s)
            else :
                break

        # Replace the selection with transformed text
        self.view.replace(edit, region, s)
