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


def git_fetch(files):
    """
    entry point for --fetch
    """
    dict_repo_with_stash = {}
    dict_repo_with_push = {}
    dict_repo_with_uncommited = {}
    dict_repo_with_unstaged = {}
    dict_repo_with_untracked = {}
    dict_repo_with_special_branches = {}
    for repo in files:
        repo = absolute_path_without_git(repo)
        if compute_args().debug:
            print("debug : " + repo + " ...")

        ############################################
        # UPDATE + FETCH
        ############################################
        command_git_check_en_print(repo, ["fetch", "--all"], True)
