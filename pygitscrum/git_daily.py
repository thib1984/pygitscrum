"""
--daily scripts
"""

from termcolor import colored
from pygitscrum.scan import absolute_path_without_git
from pygitscrum.args import compute_args
from pygitscrum.git import (
    command_git_check,
)


def git_daily(files):
    """
    entry point for --daily
    """
    since = compute_args().daily
    for repo in files:
        repo = absolute_path_without_git(repo)
        author = command_git_check(repo, ["config", "user.name"])

        log = command_git_check(
            repo,
            [
                "--no-pager",
                "log",
                "--since=" + since,
                "--branches=*",
                "--date=format:%Y-%m-%d %H:%M",
                "--author=" + author.rstrip(),
                "--format=%ad - %h --- %s",
                "--date-order",
                "--reverse",
            ],
        )
        if log != "":
            print(colored(repo, "green"))
            print(colored(log, "yellow").rstrip())
