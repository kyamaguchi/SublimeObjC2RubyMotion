class CustomTestCase(object):
    def assertSentence(self, result, expected):
        try:
            self.assertEqual(result, expected)
        except AssertionError as e:
            e.args = (e.args[0].replace("\\n", "\n"),) # edit the exception's message
            raise
