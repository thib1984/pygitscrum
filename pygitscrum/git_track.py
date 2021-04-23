from termcolor import colored
from pygitscrum.git import (
    command_git_call,
    command_git_call_print,
    command_git_check,
    command_git_check_en,
    command_git_check_en_print,
    command_git_check_print,
)


def git_track(files):
    files_to_work = []
    # boucler repos git
    for repo in files:
        command_git_check_en_print(
            repo, ["remote", "update", "--prune"], True
        )

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
                # print(line_remote_branche.split()[0])
                local_branche_track = line_remote_branche.replace(
                    "origin/", "", 1
                )
                remote_branch_to_track = line_remote_branche
                command_git_check_en_print(
                    repo,
                    [
                        "branch",
                        "--track",
                        local_branche_track.strip(" "),
                        remote_branch_to_track.strip(" "),
                    ],
                    True,
                )
        command_git_check_en_print(repo, ["remote", "update"], True)
        command_git_check_en_print(repo, ["fetch", "--all"], True)
