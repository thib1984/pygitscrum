"""
--search scripts
"""

from pygitscrum.scan import absolute_path_without_git, update_dict
from pygitscrum.print import (
    print_resume_map,
    print_debug,
    print_g,
    print_y,
)
from pygitscrum.git import (
    git_output,
)
from pygitscrum.args import compute_args


def git_search(files):
    """
    entry point for --search
    """
    print_g("Job --search started")
    print_g("git repos found : " + str(len(files)))
    print_g("running...")
    keys = compute_args().search
    dict_repo_with_commits = {}
    for repo in files:
        repo = absolute_path_without_git(repo)
        print_debug(repo + " ... ")
        first = True
        log = git_output(
            repo,
            [
                "--no-pager",
                "log",
                "--branches=*",
                "--date=format:%Y-%m-%d %H:%M",
                "--all",
                "--format=%ad - %h --- %S- %s - %ae - %aN",
                "--date-order",
            ],
        )
        if log != "":
            for line_log in log.split("\n"):
                full_find=True
                for keyword in keys:
                    if not keyword.lower() in line_log.lower():
                        full_find=False
                if full_find:
                    print_debug(line_log + "contains " + keyword)
                    if not compute_args().fast:
                        if first:
                            print_g(repo)
                            first = False
                        print_y(line_log.strip())
                    dict_repo_with_commits = update_dict(
                        repo, dict_repo_with_commits
                    )

    print_resume_map(
        dict_repo_with_commits, "repos avec commits trouves"
    )
    print("")
    if len(dict_repo_with_commits) == 0:
        print_y("No commits found...")
        print("")
    print_g("Job finished")