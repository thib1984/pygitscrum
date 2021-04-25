"""
--wip scripts
"""

from pygitscrum.git import git_code_silent
from pygitscrum.scan import (
    absolute_path_without_git,
)
from pygitscrum.print import print_debug, print_g


def git_fetch(files):
    """
    entry point for --fetch
    """
    print_g("Job --fetch started")
    print_g("git repos found : " + str(len(files)))
    print_g("running...")
    for repo in files:
        repo = absolute_path_without_git(repo)
        print_debug(repo + " ... ")
        git_code_silent(repo, ["fetch", "--all", "--prune"])
    print("")
    print_g("Job finished")