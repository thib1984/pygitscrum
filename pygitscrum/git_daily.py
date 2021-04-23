from termcolor import colored
from pygitscrum.args import compute_args
from pygitscrum.git import (
    command_git_call,
    command_git_call_print,
    command_git_check,
    command_git_check_en,
    command_git_check_en_print,
    command_git_check_print,
)


def git_daily(files):
    since = compute_args().daily
    for repo in files:
        me = command_git_check(repo, ["config", "user.name"])

        log = command_git_check(
            repo,
            [
                "--no-pager",
                "log",
                "--since=" + since,
                # "--all",  # ? (permet de voir ce qu'on n'a pas récupéré?) refs/stash
                "--branches=*",
                "--author=" + me.rstrip(),
                "--format=%ad - %h --- %s",
                "--date-order",
                "--date=short",
                "--reverse",
            ],
        )
        if log != "":
            print(colored(repo, "green"))
            print(colored(log, "yellow").rstrip())