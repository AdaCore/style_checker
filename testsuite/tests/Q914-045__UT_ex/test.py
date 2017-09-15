from support import *

class TestRun(TestCase):
    def test_quote_arg_empty_arg(self):
        self.enable_unit_test()

        from asclib.ex import quote_arg
        self.assertEqual(quote_arg(''), "''")

    def test_quote_arg_single_quote(self):
        self.enable_unit_test()

        from asclib.ex import quote_arg
        self.assertEqual(quote_arg("'"), r"''\'''")

    def test_quote_arg_newline(self):
        self.enable_unit_test()

        from asclib.ex import quote_arg
        self.assertEqual(quote_arg('\n'), r"''\n''")


if __name__ == '__main__':
    runtests()
