import os
import subprocess
from pygitscrum.args import compute_args


def command_git_check_en(repo, params):
    return command_git_check_en_print(repo, params, False)


def command_git_check_en_print(repo, params, display):
    new_env = dict(os.environ)
    new_env["LC_ALL"] = "EN"
    params_git = ["git", "-C", repo + "/.."]

    try:
        ligne_commande = params_git + params
        if display and compute_args().debug:
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
        if display and compute_args().debug:
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
    if display and compute_args().debug:
        print("debug : " + str(ligne_commande))
    subprocess.call(params_git + params)
