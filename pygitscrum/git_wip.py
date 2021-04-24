"""
--wip scripts
"""

import sys
from termcolor import colored
from pygitscrum.git import (
    command_git_check,
    command_git_check_en_print,
)
from pygitscrum.scan import (
    absolute_path_without_git,
    print_repo_if_first,
    update_dict,
)
from pygitscrum.args import compute_args
from pygitscrum.print import print_resume_map


def git_wip(files):
    """
    entry point for --wip
    """
    dict_repo_with_stash = {}
    dict_repo_with_push = {}
    dict_repo_with_uncommited = {}
    dict_repo_with_unstaged = {}
    dict_repo_with_untracked = {}
    for repo in files:
        repo = absolute_path_without_git(repo)
        if compute_args().debug:
            print("debug : " + repo + " ...")

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
        files_untracked = command_git_check(
            repo, ["ls-files", "--others", "--exclude-standard"]
        )
        first = True
        if wip_stash != "":
            for line in wip_stash.split("\n"):
                if "stash" in line:
                    if not compute_args().fast:
                        first = print_repo_if_first(first, repo)
                        print(
                            colored("wait stash - " + line, "yellow")
                        )
                    dict_repo_with_stash = update_dict(
                        repo, dict_repo_with_stash
                    )
        if diff_branches != "":
            for line in diff_branches.split("\n"):
                if "[ahead " in line:
                    if not compute_args().fast:
                        first = print_repo_if_first(first, repo)
                        print(
                            colored(
                                "wait push branch - " + line,
                                "yellow",
                            )
                        )
                        dict_repo_with_push = update_dict(
                            repo, dict_repo_with_push
                        )

        if files_unstaged != "":
            if not compute_args().fast:
                first = print_repo_if_first(first, repo)
                print(
                    colored(
                        str(len(files_unstaged.split("\n")) - 1)
                        + " files unstaged",
                        "yellow",
                    )
                )
                dict_repo_with_unstaged[repo] = (
                    len(files_unstaged.split("\n")) - 1
                )

        if files_uncommited != "":
            if not compute_args().fast:
                first = print_repo_if_first(first, repo)
                print(
                    colored(
                        str(len(files_uncommited.split("\n")) - 1)
                        + " files uncommited",
                        "yellow",
                    )
                )
                dict_repo_with_uncommited[repo] = (
                    len(files_uncommited.split("\n")) - 1
                )

        if files_untracked != "":
            if not compute_args().fast:
                first = print_repo_if_first(first, repo)
                print(
                    colored(
                        str(len(files_untracked.split("\n")))
                        + " files untracked",
                        "yellow",
                    )
                )
                dict_repo_with_untracked[repo] = len(
                    files_untracked.split("\n")
                )

    ############################################
    print_resume_map(dict_repo_with_stash, "Repos with stash")
    print_resume_map(
        dict_repo_with_push,
        "Repos with available push on one branche",
    )
    print_resume_map(
        dict_repo_with_uncommited, "Repos with uncommited files"
    )
    print_resume_map(
        dict_repo_with_unstaged, "Repos with unstaged files"
    )
    print_resume_map(
        dict_repo_with_untracked, "Repos with untracked files"
    )
