"""
--search scripts
"""

from termcolor import colored
from pygitscrum.scan import absolute_path_without_git, update_dict
from pygitscrum.print import print_resume_map
from pygitscrum.git import (
    command_git_check,
)
from pygitscrum.args import compute_args


def git_search(files):
    """
    entry point for --search
    """
    keyword = compute_args().search.lower()
    dict_repo_with_commits = {}
    for repo in files:
        repo = absolute_path_without_git(repo)
        first = True
        log = command_git_check(
            repo,
            [
                "--no-pager",
                "log",
                "--branches=*",
                "--date=format:%Y-%m-%d %H:%M",
                "--all",
                "--format=%ad - %h --- %S- %s - %ae - %aN",
                "--date-order",
            ],
        )
        if log != "":
            for line_log in log.split("\n"):
                if keyword in line_log.lower():
                    if not compute_args().fast:
                        if first:
                            print(colored(repo, "green"))
                            first = False
                        print(colored(line_log.strip(), "yellow"))
                    dict_repo_with_commits = update_dict(
                        repo, dict_repo_with_commits
                    )

    print_resume_map(
        dict_repo_with_commits, "repos avec commits trouves"
    )
