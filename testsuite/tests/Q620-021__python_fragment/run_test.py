def test_conf_py(style_checker):
    """Run checker against conf.py
    """
    p = style_checker.run_style_checker('gnat', 'conf.py')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
conf.py:58:9: E722 do not use bare 'except'
conf.py:113:1: F821 undefined name 'tags'
""")


def test_conf_frag_py(style_checker):
    """Run checker against conf.frag.py
    """
    p = style_checker.run_style_checker('dummy', 'conf.frag.py')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_conf_with_frag_keyword_py(style_checker):
    """Run checker against conf-with-frag-keyword.py
    """
    p = style_checker.run_style_checker('dummy', 'conf-with-frag-keyword.py')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_conf_bad_pep8_frag_py(style_checker):
    """Run checker against conf-bad-pep8.frag.py
    """
    p = style_checker.run_style_checker('gnat', 'conf-bad-pep8.frag.py')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
conf-bad-pep8.frag.py:10:16: E211 whitespace before '('
conf-bad-pep8.frag.py:58:9: E722 do not use bare 'except'
""")
