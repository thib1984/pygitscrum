import glob
from termcolor import colored
import os
from pygitscrum.args import compute_args


def scan_directories():
    pathname = compute_args().to_path + "/**/.git"
    files = glob.glob(pathname, recursive=True)
    files.sort()
    print(
        colored(
            "launch from : "
            + os.path.abspath(compute_args().to_path),
            "yellow",
        )
    )
    return files


def absolute_path_without_git(directory):
    return os.path.abspath(directory + "/..")
