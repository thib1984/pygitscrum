"""
--prune scripts
"""
from pygitscrum.git import git_output, git_code
from pygitscrum.scan import (
    absolute_path_without_git,
    print_repo_if_first,
    update_dict,
)
from pygitscrum.args import compute_args
from pygitscrum.print import (
    print_resume_map,
    print_debug,
    print_y,
    print_g,
)


def git_prune(files):
    """
    entry point for --prune
    """
    print_g("Job --prune started")
    print_g("git repos found : " + str(len(files)))
    print_g("running...")
    map_repo_with_gone_branches = {}

    for repo in files:
        repo = absolute_path_without_git(repo)
        print_debug(repo + " ... ")
        diff_branches = git_output(
            repo,
            [
                "for-each-ref",
                "--format=%(refname:short) %(upstream:track) (upstream:remotename)",
                "refs/heads",
            ],
        )

        first = True

        if diff_branches != "":
            for line in diff_branches.split("\n"):
                if "[gone]" in line:
                    print_debug(line + " contains [gone] ")
                    if not compute_args().fast:
                        first = print_repo_if_first(first, repo)
                        print_y("gone branch - " + line)
                        branch = line.split(" ")[0]
                        deleted = False
                        if delete(branch) == "y":
                            if git_delete(repo, branch):
                                deleted = True
                            else:
                                if forcedelete(branch) == "y":
                                    if git_force_delete(repo, branch):
                                        deleted = True
                        if not deleted:
                            map_repo_with_gone_branches = update_dict(
                                repo, map_repo_with_gone_branches
                            )
                    else:
                        map_repo_with_gone_branches = update_dict(
                            repo, map_repo_with_gone_branches
                        )

    print_resume_map(
        map_repo_with_gone_branches,
        "Repos with gone branches",
    )
    print("")
    if len(map_repo_with_gone_branches) == 0:
        print_g("No (remaining) gone branch found")
        print("")
    print_g("Job finished")


def forcedelete(branch_local):
    answer = input(
        "do you want try to FORCE delete the branch "
        + branch_local
        + " (y/N) ? "
    )
    return answer


def delete(branch_local):
    answer = input(
        "do you want try to delete the branch "
        + branch_local
        + " (y/N) ? "
    )
    return answer


def git_delete(repo, branch):
    return git_code(repo, ["branch", "-d", branch]) == 0


def git_force_delete(repo, branch):
    return git_code(repo, ["branch", "-D", branch]) == 0
