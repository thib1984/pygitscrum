"""
--wip scripts
"""
from pygitscrum.git import git_output
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


def git_wip(files):
    """
    entry point for --wip
    """
    dict_repo_with_stash = {}
    dict_repo_with_push = {}
    dict_repo_with_uncommited = {}
    dict_repo_with_unstaged = {}
    dict_repo_with_untracked = {}
    dict_repo_with_special_branches = {}
    map_repo_with_only_local_branches = {}
    for repo in files:
        repo = absolute_path_without_git(repo)
        print_debug(repo + " ... ")

        ############################################
        # STASH + DIFF BRANCHES
        ############################################
        wip_stash = git_output(repo, ["stash", "list"])
        diff_branches = git_output(
            repo,
            [
                "for-each-ref",
                '--format="%(refname:short) %(upstream:track) (upstream:remotename)"'
                "refs/heads",
            ],
        )
        diff_branches_2 = git_output(
            repo,
            [
                "branch",
                "--format=%(refname:short) %(upstream)",
            ],
        )
        files_unstaged = git_output(repo, ["diff", "--name-only"])
        files_uncommited = git_output(
            repo, ["diff", "--staged", "--name-only"]
        )
        files_untracked = git_output(
            repo, ["ls-files", "--others", "--exclude-standard"]
        )
        first = True
        branch = git_output(
            repo, ["branch", "--show-current"]
        ).rstrip()
        if branch not in ["master", "develop", "main", "dev"]:
            dict_repo_with_special_branches[repo] = branch
            if not compute_args().fast:
                print_debug(
                    "the branch " + branch + "seems be special"
                )
                first = print_repo_if_first(first, repo)
                print_y(
                    "/!\ branch = "
                    + dict_repo_with_special_branches[repo]
                )
        if wip_stash != "":
            for line in wip_stash.split("\n"):
                if "stash" in line:
                    print_debug("line " + line + " contains : stash")
                    if not compute_args().fast:
                        first = print_repo_if_first(first, repo)
                        print_y("wait stash - " + line)
                    dict_repo_with_stash = update_dict(
                        repo, dict_repo_with_stash
                    )
        if diff_branches != "":
            for line in diff_branches.split("\n"):
                if "[ahead " in line:
                    print_debug(
                        "line "
                        + line
                        + " seems indicate a pushable branch"
                    )
                    if not compute_args().fast:
                        first = print_repo_if_first(first, repo)
                        print_y("wait push branch - " + line)
                    dict_repo_with_push = update_dict(
                        repo, dict_repo_with_push
                    )

        if diff_branches_2 != "":
            for line in diff_branches_2.split("\n"):
                if "refs/remotes" not in line and line != "":
                    print_debug(
                        "line "
                        + line
                        + " seems indicate a only local branch"
                    )
                    if not compute_args().fast:
                        first = print_repo_if_first(first, repo)
                        print_y("local only branch - " + line)
                    map_repo_with_only_local_branches = update_dict(
                        repo, map_repo_with_only_local_branches
                    )

        if files_unstaged != "":
            print_debug("files_unstaged detected!")
            if not compute_args().fast:
                first = print_repo_if_first(first, repo)
                print_y(
                    str(len(files_unstaged.split("\n")) - 1)
                    + " files unstaged"
                )
            dict_repo_with_unstaged[repo] = (
                len(files_unstaged.split("\n")) - 1
            )

        if files_uncommited != "":
            print_debug("files files_uncommited detected!")
            if not compute_args().fast:
                first = print_repo_if_first(first, repo)
                print_y(
                    str(len(files_uncommited.split("\n")) - 1)
                    + " files uncommited"
                )
            dict_repo_with_uncommited[repo] = (
                len(files_uncommited.split("\n")) - 1
            )

        if files_untracked != "":
            print_debug("files untracked detected!")
            if not compute_args().fast:
                first = print_repo_if_first(first, repo)
                print_y(
                    str(len(files_untracked.split("\n")) - 1)
                    + " files untracked"
                )
            dict_repo_with_untracked[repo] = (
                len(files_untracked.split("\n")) - 1
            )

    ############################################
    print_resume_map(dict_repo_with_stash, "Repos with stash")
    print_resume_map(
        dict_repo_with_push,
        "Repos with available push on one branche",
    )
    print_resume_map(
        map_repo_with_only_local_branches,
        "Repos with local only branches ",
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
    if len(dict_repo_with_special_branches.values()) != 0:
        print("")
        print_g("Repos with special branches : ")
        for key in dict_repo_with_special_branches:
            print_y(
                key + " --> " + dict_repo_with_special_branches[key]
            )
