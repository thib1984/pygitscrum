from termcolor import colored
from pygitscrum.git import (
    command_git_call,
    command_git_call_print,
    command_git_check,
    command_git_check_en,
    command_git_check_en_print,
    command_git_check_print,
)
from pygitscrum.args import compute_args


def git_search(files):
    keyword = compute_args().search.lower()
    for repo in files:
        first = True
        log = command_git_check(
            repo,
            [
                "--no-pager",
                "log",
                # ou --all? refs/stash
                "--all",
                "--format=%ad - %h --- %S- %s - %ae - %aN",
                "--date-order",
                "--date=short",
                "--reverse",
            ],
        )
        if log != "":
            for line_log in log.split("\n"):
                if keyword in line_log.lower():
                    if first:
                        print(colored(repo, "green"))
                        first = False
                    print(colored(line_log.strip(), "yellow"))