from shutil import move
from support import *

class TestRun(TestCase):
    def test_image_ok_1_gif(self):
        """Run checker against image-ok-1.gif
        """
        p = self.run_style_checker('gnat', 'image-ok-1.gif')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_image_ok_2_jpg(self):
        """Run checker against image-ok-2.jpg
        """
        p = self.run_style_checker('gnat', 'image-ok-2.jpg')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)


if __name__ == '__main__':
    runtests()
