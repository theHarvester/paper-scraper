import requests
import re
from urllib import parse
from download.image import download as image_download

from pathlib import Path, PurePath


def download(url: str, base_path: str):
    urls = find_img_urls(url)
    for tmp_url in urls:
        filename = filename_from_url(tmp_url)
        filename = filename.replace("/", "_")
        filename = filename.replace("\\", "_")
        path = PurePath(base_path, filename)
        image_download(tmp_url, str(path))


def filename_from_url(url: str) -> str:
    parse_object = parse.urlparse(url)
    return str(parse_object.path)[1:]


def find_img_urls(url: str) -> list:
    parse_object = parse.urlparse(url)
    if parse_object.netloc == "i.imgur.com":
        filename = str(parse_object.path)
        extension = filename[-4:]
        if extension == '.jpg' or extension == '.png':
            return ["http://i.imgur.com" + filename]
    elif parse_object.netloc == "imgur.com":
        r = requests.get(url)

        urls = re.findall('meta\s+property="og:image"\s+content="([^"]+)', str(r.content))
        urls = [x for x in urls if "?fb" not in x]
        if urls:
            return urls

        link = re.findall('link\s+rel="image_src"\s+href="([^"]+)', str(r.content))
        if link:
            return link
    return [url]

