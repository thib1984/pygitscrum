"""
--track scripts
"""

from pygitscrum.git import git_output, git_code
from pygitscrum.scan import (
    absolute_path_without_git,
    print_repo_if_first,
)
from pygitscrum.print import print_debug, print_g


def git_track(files):
    """
    entry point for --track
    """

    for repo in files:
        repo = absolute_path_without_git(repo)
        print_debug(repo + " ... ")

        ############################################
        # ADD NEW ORGIN BRANCHS
        ############################################
        remote_tracking_branches = git_output(repo, ["branch", "-r"])
        local_branches = git_output(repo, ["branch", "-vv"])
        first = True
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
                first = print_repo_if_first(first, repo)
                new_local_tracking_branche = (
                    line_remote_branche.replace(
                        "origin/", "", 1
                    ).strip(" ")
                )
                remote_branch_to_track = line_remote_branche.strip(
                    " "
                )
                print_debug(
                    "the branch "
                    + remote_branch_to_track
                    + " does not exist in local"
                )
                git_code(
                    repo,
                    [
                        "branch",
                        "--track",
                        new_local_tracking_branche,
                        remote_branch_to_track,
                    ],
                )
