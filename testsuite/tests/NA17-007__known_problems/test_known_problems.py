from shutil import move


def test_known_problems_7_4(style_checker):
    """Run checker against known-problems-7.4
    """
    p = style_checker.run_style_checker('unimportant', 'known-problems-7.4')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)
