"""
pygitscrum scripts
"""

from shutil import which
import subprocess
import glob
import os
from termcolor import colored


def pygitscrum():
    """
    entry point from pygitscrum
    """

    # binaire git
    print(which("git"))

    # display git version
    params = ["git", "--version"]
    subprocess.check_call(params)
    # rechercher repos git
    directory = "."
    pathname = directory + "/**/.git"
    files = glob.glob(pathname, recursive=True)
    # print(files)
    files_to_work = []
    # boucler repos git
    for repo in files:
        print(colored(repo, "blue"))

        command_git_check(repo, ["remote", "update"])
        command_git_check(repo, ["fetch"])
        while not "Your branch is up to date" in command_git_check(
            repo, ["status"]
        ):
            print(
                colored(command_git_check(repo, ["status"]), "yellow")
            )
            answer = input("p(ull)/P(ush)/s(how)/S(how)/q(uit)")
            if answer == "p":
                command_git_call(repo, ["pull"])
            if answer == "P":
                command_git_call(repo, ["push"])
            if answer == "S":
                command_git_call(
                    repo, ["log", "-p", "HEAD..FETCH_HEAD"]
                )
                command_git_call(
                    repo, ["log", "-p", "FETCH_HEAD..HEAD"]
                )
            if answer == "s":
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
            if answer == "q":
                files_to_work.append(repo)
                break

    if len(files_to_work) > 0:
        print(
            colored(
                "Il vous reste à corriger les problemes dans : \n"
                + "\n".join(files_to_work),
                "yellow",
            )
        )


def command_git_check(repo, params):
    new_env = dict(os.environ)
    new_env["LC_ALL"] = "EN"
    params_git = ["git", "-C", repo + "/.."]
    try:
        return subprocess.check_output(
            params_git + params, env=new_env
        ).decode("utf-8")
    except subprocess.CalledProcessError as err:
        return ""


def command_git_call(repo, params):
    new_env = dict(os.environ)
    new_env["LC_ALL"] = "EN"
    params_git = ["git", "-C", repo + "/.."]
    subprocess.call(params_git + params, env=new_env)
