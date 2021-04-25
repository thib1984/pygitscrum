"""
--wip scripts
"""
from pygitscrum.git import git_code, git_code_silent
from pygitscrum.scan import absolute_path_without_git
from pygitscrum.args import compute_args
from pygitscrum.print import (
    print_debug,
    print_resume_list,
    print_g,
)


def git_show(files):
    """
    entry point for --wip
    """
    files_to_work = []
    for repo in files:
        repo = absolute_path_without_git(repo)
        print_debug(repo + " ... ")
        item = compute_args().show
        if (
            git_code_silent(
                repo,
                [
                    "show",
                    item,
                ],
            )
            == 0
        ):
            print_debug(
                "repo " + repo + " contains the object " + item
            )
            if not compute_args().fast:
                print_g(repo)
                answer = input("see the object (Y/n) ? ")
                if answer.lower() in ["y", ""]:

                    git_code(
                        repo,
                        [
                            "show",
                            item,
                        ],
                    )

            files_to_work.append(repo)

    ############################################
    print_resume_list(files_to_work, "Repos with given object")
