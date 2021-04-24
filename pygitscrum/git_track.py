"""
--track scripts
"""

from pygitscrum.git import (
    command_git_check_en,
    command_git_check_en_print,
)
from pygitscrum.scan import absolute_path_without_git
from pygitscrum.args import compute_args
from termcolor import colored


def git_track(files):
    """
    entry point for --track
    """
    print(
        colored(
            "/!\ If you accept the launch, you will update, PRUNE and fetch the refs branches in your system",
            "red",
        )
    )
    answer = input("Do you confirm (Y/n) ? ")
    if not (answer.lower() == "" or answer.lower() == "y"):
        print(colored("Cancelled operation", "green"))
        exit(1)
    for repo in files:
        repo = absolute_path_without_git(repo)
        if compute_args().debug:
            print("debug : " + repo + " ...")

        ############################################
        # UPDATE + PRUNE + FETCH
        ############################################
        command_git_check_en_print(repo, ["remote", "update"], True)
        command_git_check_en_print(
            repo, ["remote", "update", "--prune"], True
        )
        command_git_check_en_print(repo, ["fetch", "--all"], True)

        ############################################
        # ADD NEW ORGIN BRANCHS
        ############################################
        remote_tracking_branches = command_git_check_en(
            repo, ["branch", "-r"]
        )
        local_branches = command_git_check_en(repo, ["branch", "-vv"])

        for line_remote_branche in remote_tracking_branches.split(
            "\n"
        ):
            # pas de ligne vide, pas de HEAD
            if (
                line_remote_branche != ""
                and "->" not in line_remote_branche
                and line_remote_branche.split()[0]
                not in local_branches
            ):
                new_local_tracking_branche = (
                    line_remote_branche.replace(
                        "origin/", "", 1
                    ).strip(" ")
                )
                remote_branch_to_track = line_remote_branche.strip(
                    " "
                )
                command_git_check_en_print(
                    repo,
                    [
                        "branch",
                        "--track",
                        new_local_tracking_branche,
                        remote_branch_to_track,
                    ],
                    True,
                )

        ############################################
        # UPDATE + PRUNE + FETCH
        ############################################
        command_git_check_en_print(repo, ["remote", "update"], True)
        command_git_check_en_print(repo, ["fetch", "--all"], True)
