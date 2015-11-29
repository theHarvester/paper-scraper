import requests
from pathlib import Path
import os


def download(url: str, path: str):
    r = requests.get(url, stream=True)
    extension = get_extension(r.headers['Content-Type'])
    if not extension:
        return None
    path = replace_extension(path, extension)

    ensure_path(path)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()


def get_extension(content_type):
    switcher = {
        "image/jpeg": "jpg",
        "image/jpg": "jpg",
        "image/png": "png",
        "image/gif": "gif",
    }
    return switcher.get(content_type, None)


def replace_extension(path: str, new_extension: str) -> str:
    return os.path.splitext(path)[0] + '.' + new_extension


def ensure_path(path: str):
    posix_path = Path(path)
    for x in reversed(posix_path.parents):
        tmp_path = Path(x)
        if not tmp_path.exists():
            tmp_path.mkdir()
