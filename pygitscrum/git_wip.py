"""
--wip scripts
"""

from termcolor import colored
from pygitscrum.git import (
    command_git_check,
    command_git_check_en_print,
)
from pygitscrum.scan import (
    absolute_path_without_git,
    print_repo_if_first,
)
from pygitscrum.args import compute_args


def git_wip(files):
    """
    entry point for --wip
    """
    for repo in files:
        if compute_args().debug:
            print(
                "debug : " + absolute_path_without_git(repo) + " ..."
            )

        ############################################
        # UPDATE + FETCH
        ############################################
        command_git_check_en_print(repo, ["remote", "update"], True)
        command_git_check_en_print(repo, ["fetch", "--all"], True)

        ############################################
        # STASH + DIFF BRANCHES
        ############################################

        wip_stash = command_git_check(repo, ["stash", "list"])
        diff_branches = command_git_check(
            repo,
            [
                "for-each-ref",
                '--format="%(refname:short) %(upstream:track) (upstream:remotename)"'
                "refs/heads",
            ],
        )
        files_unstaged = command_git_check(
            repo, ["diff", "--name-only"]
        )
        files_uncommited = command_git_check(
            repo, ["diff", "--staged", "--name-only"]
        )
        first = True
        if wip_stash != "":
            for line in wip_stash.split("\n"):
                if "stash" in line:
                    first = print_repo_if_first(first, repo)
                    print(colored("wait stash - " + line, "yellow"))
        if diff_branches != "":
            for line in diff_branches.split("\n"):
                if "[ahead " in line:
                    first = print_repo_if_first(first, repo)
                    print(
                        colored(
                            "wait push branch - " + line,
                            "yellow",
                        )
                    )

        if files_unstaged != "":
            first = print_repo_if_first(first, repo)
            print(
                colored(
                    str(len(files_unstaged.split("\n")) - 1)
                    + " files unstaged",
                    "yellow",
                )
            )

        if files_uncommited != "":
            first = print_repo_if_first(first, repo)
            print(
                colored(
                    str(len(files_uncommited.split("\n")) - 1)
                    + " files uncommited",
                    "yellow",
                )
            )
