"""
pygitscrum scripts
"""

from shutil import which
import subprocess
import glob
import os
from termcolor import colored
import sys
import pkg_resources


def pygitscrum():
    """
    entry point from pygitscrum
    """

    # binaire git
    # print(which("git"))

    # display git version
    # params = ["git", "--version"]
    # subprocess.check_call(params)
    # rechercher repos git
    directory = "."
    pathname = directory + "/**/.git"
    files = glob.glob(pathname, recursive=True)
    files.sort()
    # print(files)

    if len(sys.argv) < 2 or (sys.argv[1] == "--help"):
        print(
            """
        NAME
            pygitscrum

        SYNOPSIS:
            with pygitscrum you can masterize few git actions

        USAGE: pygitscrum [OPTION] [PARAMETER]

            --check     : check your repos one by one, fetch them, and ask you if a pull/push is available
                        you can also pull/push or check the differences
            --daily     : check your repos one by one, and print the recents commits since yesterday
            --search    : check in all repos and print the logs with the key word in parameter
            --help      : display this help message
            --update    : update this programm
            --version   : display the version

        Full documentation at: <https://github.com/thib1984/ytdlmusic>
        Report bugs to <https://github.com/thib1984/ytdlmusic/issues>

        MIT Licence.
        Copyright (c) 2021 thib1984.
        This is free software: you are free to change and redistribute it.
        There is NO WARRANTY, to the extent permitted by law.

        Written by thib1984."""
        )
    elif sys.argv[1] == "--version":
        print(
            "version pygitscrum : "
            + pkg_resources.get_distribution("pygitscrum").version
        )
    elif sys.argv[1] == "--update":
        prog = "pip3"
        if (which("pip3")) is None:
            prog = "pip"
        params = [
            prog,
            "install",
            "--upgrade",
            "pygitscrum",
        ]
        subprocess.check_call(params)

    elif sys.argv[1] == "--check":
        files_to_work = []
        # boucler repos git
        print(
            colored(
                "check all repos in current directory...", "green"
            )
        )
        for repo in files:
            print(colored(repo, "blue"))

            # quelle difference?
            # comment forcer la récuperation des branches distantes?
            command_git_check_en(repo, ["remote", "update"])
            command_git_check_en(repo, ["fetch", "--all"])
            while (
                not "Your branch is up to date"
                in command_git_check_en(repo, ["status"])
            ):
                print(
                    colored(
                        command_git_check_en(repo, ["status"]),
                        "yellow",
                    )
                )
                answer = input(
                    "p(ull)/P(ush)/s(how)/S(how all)/q(uit)? "
                )
                if answer == "p":
                    command_git_call(repo, ["pull"])
                elif answer == "P":
                    command_git_call(repo, ["push"])
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

    elif sys.argv[1] == "--daily":
        print(colored("check for the daily...", "green"))
        for repo in files:
            me = command_git_check(repo, ["config", "user.name"])
            log = command_git_check(
                repo,
                [
                    "--no-pager",
                    "log",
                    "--since=yesterday",
                    # ou --all?
                    "--branches=*",
                    "--author=" + me.rstrip(),
                    "--format=%ad - %h --- %s",
                    "--date-order",
                    "--date=short",
                    "--reverse",
                ],
            )
            if log != "":
                print(colored(repo, "blue"))
                print(colored(log, "yellow").rstrip())

    elif sys.argv[1] == "--search":
        print(
            colored(
                "search " + sys.argv[1] + " in logs of all repos",
                "green",
            )
        )
        for repo in files:
            first = True
            log = command_git_check(
                repo,
                [
                    "--no-pager",
                    "log",
                    # ou --all?
                    "--branches=*",
                    "--format=%ad - %h --- %S- %s - %ae - %aN",
                    "--date-order",
                    "--date=short",
                    "--reverse",
                ],
            )
            if log != "":
                for item in log.split("\n"):
                    if sys.argv[2] in item:
                        if first:
                            print(colored(repo, "blue"))
                            first = False
                        print(colored(item.strip(), "yellow"))


def command_git_check_en(repo, params):
    new_env = dict(os.environ)
    new_env["LC_ALL"] = "EN"
    params_git = ["git", "-C", repo + "/.."]
    try:
        return subprocess.check_output(
            params_git + params, env=new_env
        ).decode("utf-8")
    except subprocess.CalledProcessError as err:
        return ""


def command_git_check(repo, params):
    params_git = ["git", "-C", repo + "/.."]
    try:
        return subprocess.check_output(params_git + params).decode()
    except subprocess.CalledProcessError as err:
        return ""


def command_git_call(repo, params):
    # new_env = dict(os.environ)
    # new_env["LC_ALL"] = "EN"
    params_git = ["git", "-C", repo + "/.."]
    subprocess.call(params_git + params)
