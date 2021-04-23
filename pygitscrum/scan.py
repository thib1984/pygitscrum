import glob
from termcolor import colored
import os


def scan_directories():
    directory = "."
    pathname = directory + "/**/.git"
    files = glob.glob(pathname, recursive=True)
    files.sort()
    print(
        colored(
            "launch from : " + os.path.abspath(directory), "yellow"
        )
    )
    return files