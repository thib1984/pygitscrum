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
    update_dict,
)
from pygitscrum.args import compute_args
from pygitscrum.print import print_resume_map


def git_prune(files):
    """
    entry point for --prune
    """

    map_repo_with_stash = {}
    map_repo_with_gone_branches = {}
    for repo in files:
        repo = absolute_path_without_git(repo)
        if compute_args().debug:
            print("debug : " + repo + " ...")

        ############################################
        # UPDATE + FETCH
        ############################################
        # TODO identique!
        command_git_check_en_print(repo, ["remote", "update"], True)
        command_git_check_en_print(repo, ["fetch", "--all"], True)

        ############################################
        # GIT STATUS
        ############################################

        wip_stash = command_git_check(repo, ["stash", "list"])
        # TODO aussi  git branch --format "%(refname:short) %(upstream)" pour les branches jamais poussées?
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
                    if not compute_args().fast:
                        first = print_repo_if_first(first, repo)
                        print(colored("stash - " + line, "yellow"))
                    map_repo_with_stash = update_dict(
                        repo, map_repo_with_stash
                    )
        if diff_branches != "":
            for line in diff_branches.split("\n"):
                if "[gone]" in line:
                    if not compute_args().fast:
                        first = print_repo_if_first(first, repo)
                        print(
                            colored(
                                "gone branch - " + line,
                                "yellow",
                            )
                        )
                    map_repo_with_gone_branches = update_dict(
                        repo, map_repo_with_gone_branches
                    )

    print_resume_map(map_repo_with_stash, "Repos with stash")
    print_resume_map(
        map_repo_with_gone_branches,
        "Repos with gone branches",
    )
