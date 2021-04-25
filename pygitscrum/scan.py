"""
scan anf gest repo scripts
"""

import glob
import os
from pygitscrum.args import compute_args
from pygitscrum.print import print_r, print_g


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
        print_r("no found local repos!")
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
        print_g(repo)
    return first


def update_dict(repo, dict_repo_with_stash):
    if repo in dict_repo_with_stash:
        dict_repo_with_stash[repo] = dict_repo_with_stash[repo] + 1
    else:
        dict_repo_with_stash[repo] = 1
    return dict_repo_with_stash
