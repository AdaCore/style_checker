def test_quote_arg_empty_arg(style_checker):
    style_checker.enable_unit_test()

    from asclib.ex import quote_arg
    assert quote_arg('') == "''"


def test_quote_arg_single_quote(style_checker):
    style_checker.enable_unit_test()

    from asclib.ex import quote_arg
    assert quote_arg("'") == r"''\'''"


def test_quote_arg_newline(style_checker):
    style_checker.enable_unit_test()

    from asclib.ex import quote_arg
    assert quote_arg('\n') == r"''\n''"
