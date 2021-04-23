from termcolor import colored
from pygitscrum.git import (
    command_git_call,
    command_git_call_print,
    command_git_check,
    command_git_check_en,
    command_git_check_en_print,
    command_git_check_print,
)


def git_check(files):
    files_to_work = []
    # boucler repos git
    print(colored("check all repos in current directory...", "green"))
    for repo in files:
        print("debug : " + repo + " ...")

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
        while not "Your branch is up to date" in command_git_check_en(
            repo, ["status"]
        ):
            print(colored(repo, "yellow"))
            print(
                colored(
                    command_git_check_en(repo, ["status"]),
                    "yellow",
                )
            )
            answer = input("p(ull)/P(ush)/s(how)/S(how all)/q(uit)? ")
            if answer == "p":
                command_git_call_print(repo, ["pull"], True)
            elif answer == "P":
                command_git_call_print(repo, ["push"], True)
            elif answer == "S":
                command_git_call(
                    repo, ["log", "-p", "HEAD..FETCH_HEAD"]
                )
                command_git_call(
                    repo, ["log", "-p", "FETCH_HEAD..HEAD"]
                )
            elif answer == "s":
                command_git_call(
                    repo,
                    [
                        "log",
                        "-p",
                        "--name-only",
                        "HEAD..FETCH_HEAD",
                    ],
                )
                command_git_call(
                    repo,
                    [
                        "log",
                        "-p",
                        "--name-only",
                        "FETCH_HEAD..HEAD",
                    ],
                )
            else:
                files_to_work.append(repo)
                break
    if len(files_to_work) > 0:
        print("")
        print(
            colored(
                "Folders that will be checked : \n"
                + "\n".join(files_to_work),
                "yellow",
            )
        )