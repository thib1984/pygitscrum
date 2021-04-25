"""
--daily scripts
"""

from termcolor import colored
from pygitscrum.scan import absolute_path_without_git
from pygitscrum.args import compute_args
from pygitscrum.print import (
    print_resume_map,
    print_debug,
    print_g,
    print_y,
)
from pygitscrum.git import (
    git_output,
)


def git_daily(files):
    """
    entry point for --daily
    """
    since = compute_args().daily
    dict_repo_with_commits = {}
    for repo in files:
        repo = absolute_path_without_git(repo)
        print_debug(repo + " ... ")
        author = git_output(repo, ["config", "user.name"])

        log = git_output(
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
                print_g(repo)
                print_y(log.rstrip())
            dict_repo_with_commits[repo] = log.count("\n")

    print_resume_map(dict_repo_with_commits, "Repos commits")
