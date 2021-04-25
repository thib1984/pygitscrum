"""
--wip scripts
"""

from pygitscrum.git import git_code_silent
from pygitscrum.scan import (
    absolute_path_without_git,
)
from pygitscrum.print import print_debug


def git_fetch(files):
    """
    entry point for --fetch
    """
    for repo in files:
        repo = absolute_path_without_git(repo)
        print_debug(repo + " ... ")
        git_code_silent(repo, ["fetch", "--all", "--prune"])
