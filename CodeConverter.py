import re

class CodeConverter(object):
    def __init__(self, s):
        self.s = s

    def result(self):
        self.multilines_to_one_line()
        self.replace_nsstring()
        self.mark_spaces_in_string()
        self.convert_square_brackets_expression()
        self.remove_semicolon_at_the_end()
        self.remove_autorelease()
        self.remove_type_declaration()
        self.restore_spaces_in_string()
        return self.s

    # Helpers
    def convert_args(self, matchobj):
        # Consider args with colon followed by spaces
        following_args = re.sub(r'([^:]+)(\s+)(\S+):', r'\1,\3:', matchobj.group(2))
        # Clear extra spaces after colons
        following_args = re.sub(r':\s+', ':', following_args)
        return "%s(%s)" % (matchobj.group(1), following_args)

    def ruby_style_code(self, matchobj):
        msg = re.sub(r'([^:]+)\:\s*(.+)', self.convert_args, matchobj.group(2))
        return "%s.%s" % (matchobj.group(1), msg)

    def space_to_mark(self, matchobj):
        return re.sub(r' ', '__SPACE__', matchobj.group(1))

    def arrange_multilines(self, matchobj):
        if matchobj.group(2) == '}' and '{' not in matchobj.group(1):
            return matchobj.group()
        else:
            return "%s%s " % (matchobj.group(1), matchobj.group(2))

    # Conversions
    def multilines_to_one_line(self):
        # Remove trailing white space first. Refs: TrimTrailingWhiteSpace
        self.s = re.sub(r'[\t ]+$', '', self.s)
        self.s = re.sub(re.compile(r'(.*)([^;\s{])$\n^\s*', re.MULTILINE), self.arrange_multilines, self.s)
        return self

    def replace_nsstring(self):
        self.s = re.sub(r'@("(?:[^\\"]|\\.)*")', r'\1', self.s)
        return self

    def mark_spaces_in_string(self):
        self.s = re.sub(r'("(?:[^\\"]|\\.)*")', self.space_to_mark, self.s)
        return self

    def restore_spaces_in_string(self):
        self.s = re.sub(r'__SPACE__', ' ', self.s)
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
        self.s = re.sub(r'\.autorelease', '', self.s)
        return self

    def remove_type_declaration(self):
        self.s = re.sub(re.compile(r'^(\s*)[a-zA-Z_0-9]+\s*\*\s*([^=]+)=', re.MULTILINE), r'\1\2=', self.s)
        return self
