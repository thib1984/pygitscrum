"""
--check scripts
"""

from termcolor import colored
from pygitscrum.git import (
    command_git_call,
    command_git_call_print,
    command_git_check,
    command_git_check_en,
    command_git_check_en_print,
)
from pygitscrum.args import compute_args
from pygitscrum.scan import absolute_path_without_git
from pygitscrum.print import print_resume_list


def git_check(files):
    """
    entry point for --check
    """
    files_to_work = []
    for repo in files:
        repo = absolute_path_without_git(repo)
        if compute_args().debug:
            print("debug : " + repo + " ...")

        ############################################
        # UPDATE TRACKED REPOSITORY
        ############################################
        command_git_check_en_print(repo, ["fetch", "--all", "--prune"], True)
        ############################################

        ############################################
        # GIT STATUS
        ############################################
        while "Your branch is up to date" not in command_git_check_en(
            repo, ["status"]
        ):
            if compute_args().fast:
                files_to_work.append(repo)
                break
            print(colored(repo, "yellow"))
            print(
                colored(
                    command_git_check(repo, ["status"]),
                    "yellow",
                )
            )
            answer = input("p(ull)/P(ush)/s(how)/S(how all)/q(uit)? ")
            if answer == "p":
                command_git_call_print(repo, ["pull"], True)
            elif answer == "P":
                command_git_call_print(repo, ["push"], True)
            elif answer == "S":
                command_git_call(
                    repo, ["log", "-p", "HEAD..FETCH_HEAD"]
                )
                command_git_call(
                    repo, ["log", "-p", "FETCH_HEAD..HEAD"]
                )
            elif answer == "s":
                command_git_call(
                    repo,
                    [
                        "log",
                        "-p",
                        "--name-only",
                        "HEAD..FETCH_HEAD",
                    ],
                )
                command_git_call(
                    repo,
                    [
                        "log",
                        "-p",
                        "--name-only",
                        "FETCH_HEAD..HEAD",
                    ],
                )
            else:
                files_to_work.append(repo)
                break

    ############################################
    print_resume_list(files_to_work, "Repos with pull/push available")
