def test_image_ok_1_gif(style_checker):
    """Run checker against image-ok-1.gif
    """
    p = style_checker.run_style_checker('gnat', 'image-ok-1.gif')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_image_ok_2_jpg(style_checker):
    """Run checker against image-ok-2.jpg
    """
    p = style_checker.run_style_checker('gnat', 'image-ok-2.jpg')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)
