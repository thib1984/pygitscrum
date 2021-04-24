"""
--daily scripts
"""

from termcolor import colored
from pygitscrum.scan import absolute_path_without_git
from pygitscrum.args import compute_args
from pygitscrum.print import print_resume_map
from pygitscrum.git import (
    command_git_check,
)


def git_daily(files):
    """
    entry point for --daily
    """
    since = compute_args().daily
    dict_repo_with_commits = {}
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
            if not compute_args().fast:
                print(colored(repo, "green"))
                print(colored(log, "yellow").rstrip())
            dict_repo_with_commits[repo] = log.count("\n")

    print_resume_map(dict_repo_with_commits, "Repos commits")