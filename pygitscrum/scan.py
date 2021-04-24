"""
scan anf gest repo scripts
"""

import glob
import os
from termcolor import colored
from pygitscrum.args import compute_args


def scan_directories():
    """
    entry point for --scan
    """
    pathname = compute_args().to_path + "/**/.git"
    files = glob.glob(pathname, recursive=True)
    files.sort()
    if (
        len(files) == 0
        and not compute_args().update
        and not compute_args().version
    ):
        print(colored("no found local repos!", "red"))
    return files


def absolute_path_without_git(directory):
    """
    return the absolute path of local git repo
    """
    return os.path.abspath(directory + "/..")


def print_repo_if_first(first, repo):
    """
    print the repo only if first == True
    """
    if first:
        first = False
        print(
            colored(
                repo,
                "green",
            )
        )
    return first
