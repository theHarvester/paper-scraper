import unittest
import shutil
import os
from download import imgur


class TestDownloadMethods(unittest.TestCase):
    def setUp(self):
        for root, dirs, files in os.walk('tmp'):
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))

    # def tearDown(self):
    #     self.setUp()

    def test_gets_filename_from_url(self):
        self.assertEqual("test.png", imgur.filename_from_url('http://i.imgur.com/test.png'))
        # gallery http://imgur.com/gallery/rHU4IBj

    def test_gets_gallery_image_url(self):
        tmp = imgur.find_img_urls('http://imgur.com/gallery/pY3JZsH')
        self.assertEqual(['http://i.imgur.com/pY3JZsH.jpg'], tmp)

    def test_gets_single_image_url(self):
        tmp = imgur.find_img_urls('http://i.imgur.com/pY3JZsH.jpg')
        self.assertEqual(['http://i.imgur.com/pY3JZsH.jpg'], tmp)

    def test_download_plain_image(self):
        self.assertFalse(os.path.isfile("tmp/kIxNs2s.png"))
        imgur.download('http://i.imgur.com/kIxNs2s.png', 'tmp')
        self.assertTrue(os.path.isfile("tmp/kIxNs2s.png"))

    def test_download(self):
        self.assertFalse(os.path.isfile("tmp/test/pY3JZsH.jpg"))
        imgur.download("http://i.imgur.com/pY3JZsH.jpg", "tmp/test")
        self.assertTrue(os.path.isfile("tmp/test/pY3JZsH.jpg"))

    def test_download_gallery_with_multiple_images(self):
        self.assertFalse(os.path.isfile("tmp/gallery/iqbBadV.jpg"))
        # imgur.download('http://imgur.com/gallery/ZHAehn1', "tmp/gallery")
        imgur.download('http://imgur.com/gallery/zUlsR', "tmp/gallery")
        self.assertTrue(os.path.isfile("tmp/gallery/iqbBadV.jpg"))
