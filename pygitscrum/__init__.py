"""
pygitscrum scripts
"""

from shutil import which
import subprocess
import glob
import os
from termcolor import colored
import pkg_resources
import argparse


def pygitscrum():
    """
    entry point from pygitscrum
    """

    my_parser = argparse.ArgumentParser(
        description="pygitscrum : masterize git!!!",
        epilog="""
        Full documentation at: <https://github.com/thib1984/ytdlmusic>.
        Report bugs to <https://github.com/thib1984/ytdlmusic/issues>.
        MIT Licence.
        Copyright (c) 2021 thib1984.
        This is free software: you are free to change and redistribute it.
        There is NO WARRANTY, to the extent permitted by law.
        Written by thib1984.""",
    )
    my_group = my_parser.add_mutually_exclusive_group(required=True)
    my_group.add_argument(
        "-d",
        "--daily",
        metavar="since",
        action="store",
        type=str,
        nargs="?",
        const="yesterday",
        help="from scrum time, optionnal parameter : the 'since' in git format",
    )
    my_group.add_argument(
        "-s",
        "--search",
        metavar="keyword",
        action="store",
        type=str,
        help="search in the git logs the 'keyword'",
    )
    my_group.add_argument(
        "-c",
        "--check",
        action="store_true",
        help="check your repos one by one, fetch all, and ask you if a pull/push is available you can also pull/push or check the differences",
    )
    my_group.add_argument(
        "-t",
        "--track",
        action="store_true",
        help="check your repos one by one, track new branches, fetch all, and delete inexisting branches at distant",
    )
    my_group.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="display pygitscrum's version",
    )
    my_group.add_argument(
        "-u",
        "--update",
        action="store_true",
        help="update pygitscrum",
    )
    args = my_parser.parse_args()

    files = scan_directories()

    if args.version:
        version_pygitscrum()
    elif args.update:
        update_pygitscrum()
    elif args.track:
        git_track(files)
    elif args.check:
        git_check(files)
    elif args.daily:
        git_daily(files, args)
    elif args.search:
        git_search(files, args)


def newmethod699():
    my_parser = argparse.ArgumentParser(
        description="pygitscrum : masterize git!!!",
        epilog="""
        Full documentation at: <https://github.com/thib1984/ytdlmusic>.
        Report bugs to <https://github.com/thib1984/ytdlmusic/issues>.
        MIT Licence.
        Copyright (c) 2021 thib1984.
        This is free software: you are free to change and redistribute it.
        There is NO WARRANTY, to the extent permitted by law.
        Written by thib1984.""",
    )
    my_group = my_parser.add_mutually_exclusive_group(required=True)
    my_group.add_argument(
        "-d",
        "--daily",
        metavar="since",
        action="store",
        type=str,
        nargs="?",
        const="yesterday",
        help="from scrum time, optionnal parameter : the 'since' in git format",
    )
    my_group.add_argument(
        "-s",
        "--search",
        metavar="keyword",
        action="store",
        type=str,
        help="search in the git logs the 'keyword'",
    )
    my_group.add_argument(
        "-c",
        "--check",
        action="store_true",
        help="check your repos one by one, fetch all, and ask you if a pull/push is available you can also pull/push or check the differences",
    )
    my_group.add_argument(
        "-t",
        "--track",
        action="store_true",
        help="check your repos one by one, track new branches, fetch all, and delete inexisting branches at distant",
    )
    my_group.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="display pygitscrum's version",
    )
    my_group.add_argument(
        "-u",
        "--update",
        action="store_true",
        help="update pygitscrum",
    )
    args = my_parser.parse_args()
    return args


def scan_directories():
    directory = "."
    pathname = directory + "/**/.git"
    files = glob.glob(pathname, recursive=True)
    files.sort()
    print(
        colored(
            "launch from : " + os.path.abspath(directory), "yellow"
        )
    )
    return files


def git_search(files, args):
    for repo in files:
        first = True
        log = command_git_check(
            repo,
            [
                "--no-pager",
                "log",
                # ou --all? refs/stash
                "--all",
                "--format=%ad - %h --- %S- %s - %ae - %aN",
                "--date-order",
                "--date=short",
                "--reverse",
            ],
        )
        if log != "":
            for line_log in log.split("\n"):
                if args.search.lower() in line_log.lower():
                    if first:
                        print(colored(repo, "green"))
                        first = False
                    print(colored(line_log.strip(), "yellow"))


def git_daily(files, args):
    for repo in files:
        me = command_git_check(repo, ["config", "user.name"])
        log = command_git_check(
            repo,
            [
                "--no-pager",
                "log",
                "--since=" + args.daily,
                # "--all",  # ? (permet de voir ce qu'on n'a pas récupéré?) refs/stash
                "--branches=*",
                "--author=" + me.rstrip(),
                "--format=%ad - %h --- %s",
                "--date-order",
                "--date=short",
                "--reverse",
            ],
        )
        if log != "":
            print(colored(repo, "green"))
            print(colored(log, "yellow").rstrip())


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


def update_pygitscrum():
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


def version_pygitscrum():
    print(
        "version pygitscrum : "
        + pkg_resources.get_distribution("pygitscrum").version
    )


def command_git_check_en(repo, params):
    return command_git_check_en_print(repo, params, False)


def command_git_check_en_print(repo, params, display):
    new_env = dict(os.environ)
    new_env["LC_ALL"] = "EN"
    params_git = ["git", "-C", repo + "/.."]

    try:
        ligne_commande = params_git + params
        if display:
            print("debug : " + str(ligne_commande))
        return subprocess.check_output(
            ligne_commande, env=new_env
        ).decode("utf-8")
    except subprocess.CalledProcessError as err:
        return ""


def command_git_check(repo, params):
    return command_git_check_print(repo, params, False)


def command_git_check_print(repo, params, display):
    params_git = ["git", "-C", repo + "/.."]
    try:
        ligne_commande = params_git + params
        if display:
            print("debug : " + str(ligne_commande))
        return subprocess.check_output(ligne_commande).decode()
    except subprocess.CalledProcessError as err:
        return ""


def command_git_call(repo, params):
    command_git_call_print(repo, params, False)


def command_git_call_print(repo, params, display):
    # new_env = dict(os.environ)
    # new_env["LC_ALL"] = "EN"
    params_git = ["git", "-C", repo + "/.."]
    ligne_commande = params_git + params
    if display:
        print("debug : " + str(ligne_commande))
    subprocess.call(params_git + params)
