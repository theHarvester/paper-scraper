import unittest

import shutil
import os

from download import image


class TestDownloadMethods(unittest.TestCase):
    def setUp(self):
        for root, dirs, files in os.walk('tmp'):
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))

    def tearDown(self):
        self.setUp()

    def test_download(self):
        self.assertFalse(os.path.isfile("tmp/test.png"))
        image.download("http://i.imgur.com/wG51k7v.png", "tmp/test.png")
        self.assertTrue(os.path.isfile("tmp/test.png"))

    def test_ensure_path_builds_missing_folders(self):
        self.assertFalse(os.path.isdir("tmp/foo/bar/woo"))
        image.ensure_path("tmp/foo/bar/woo/something.jpg")
        self.assertTrue(os.path.isdir("tmp/foo/bar/woo"))
        self.assertFalse(os.path.isdir("tmp/bar/foo/woo"))
        image.ensure_path(os.getcwd() + "/tmp/bar/foo/woo/something.jpg")
        self.assertTrue(os.path.isdir("tmp/bar/foo/woo"))

    def test_missing_directories_are_built_when_image_downloaded(self):
        self.assertFalse(os.path.isfile("tmp/baz/test.png"))
        # image.download("http://i.imgur.com/wG51k7v.png", "tmp/baz/test.png")
        image.download("http://i.imgur.com/pY3JZsH.jpg", "tmp/baz/test.jpg")  # new
        self.assertTrue(os.path.isfile("tmp/baz/test.jpg"))


if __name__ == '__main__':
    unittest.main()
