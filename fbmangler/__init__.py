import itertools
import typing
import secrets

from iptcinfo3 import IPTCInfo
from pathlib import Path
from typing import Optional

EXTENSIONS = [".jpg"]


# Scan the file in path for Facebook tracking
def scan_file(file: Path) -> Optional[IPTCInfo]:
    if file.exists() and file.is_file() and file.suffix in EXTENSIONS:
        return IPTCInfo(file)


# Scan the directory for image files
def scan_dir(dirname: Path) -> typing.Iterator[Path]:
    return itertools.chain(*[dirname.rglob(suffix) for suffix in [f"*{suffix}" for suffix in EXTENSIONS]])


# Scan the path name for files (or file)
def scan(pathname: Path) -> typing.List[IPTCInfo]:
    files = []
    if pathname.is_file():
        files.append(scan_file(pathname))
    else:
        dirs: typing.Iterator[Path] = scan_dir(pathname)
        for d in dirs:
            files.append(scan_file(d))

    return files


def mangle(file: IPTCInfo) -> int:
    tracking: str = file['special instructions']

    if tracking is not None:
        if tracking.startswith(b'FBMD'):
            print(f'Old tracking: {file["special instructions"].decode("utf-8")}')
            file['special instructions'] = f'FBMD{secrets.token_hex(int((len(tracking) - 4) / 2))}'
            print(f'New tracking: {file["special instructions"]}')
            file.save()
            return 1
        else:
            return 0
    else:
        return 0


def main():
    path: str = input('Directory or file to scan: ').replace('\\', '/')

    location: Path = Path(path)

    infos = scan(location)

    count = 0
    for info in infos:
        count += mangle(info)

    print(f'Parsed {count} files')
