"""
--prune scripts
"""

from termcolor import colored
from pygitscrum.git import (
    command_git_check_en_print,
    command_git_check,
)
from pygitscrum.scan import (
    absolute_path_without_git,
    print_repo_if_first,
)
from pygitscrum.args import compute_args


def git_prune(files):
    """
    entry point for --prune
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
        # GIT STATUS
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

        first = True
        if wip_stash != "":
            for line in wip_stash.split("\n"):
                if "stash" in line:
                    first = print_repo_if_first(first, repo)
                    print(colored("stash - " + line, "yellow"))
        if diff_branches != "":
            for line in diff_branches.split("\n"):
                if "[gone]" in line:
                    first = print_repo_if_first(first, repo)
                    print(
                        colored(
                            "gone branch - " + line,
                            "yellow",
                        )
                    )
