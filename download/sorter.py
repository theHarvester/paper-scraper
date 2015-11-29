

def sort_img_by_size(filename):
    if filename != "":
        path = str(os.path.dirname(os.path.abspath(__file__)))
        dimensions = self.get_img_dimensions()
        width = dimensions[0]
        height = dimensions[1]
        if width >= 3840 and height >= 2160:
            move(path + '/tmp/' + filename, path + '/4k/' + self.filename)
        elif width >= 2880 and height >= 1800:
            move(path + '/tmp/' + filename, path + '/retina/' + self.filename)
        elif width >= 1920 and height >= 1080:
            move(path + '/tmp/' + filename, path + '/1080p/' + self.filename)