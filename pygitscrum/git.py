"""
git general scripts
"""

import os
import subprocess
from pygitscrum.args import compute_args


def command_git_check_en(repo, params):
    """
    command git -C repo
    return status code
    force english lang
    no print the command
    """
    return command_git_check_en_print(repo, params, False)


def command_git_check_en_print(repo, params, display):
    """
    command git -C repo
    return status code
    force english lang
    if display True, print the command
    """
    new_env = dict(os.environ)
    new_env["LC_ALL"] = "EN"
    params_git = ["git", "-C", repo]

    try:
        ligne_commande = params_git + params
        if display and compute_args().debug:
            print("debug : " + str(ligne_commande))
        return subprocess.check_output(
            ligne_commande, env=new_env
        ).decode("utf-8")
    except subprocess.CalledProcessError:
        return ""


def command_git_check(repo, params):
    """
    command git -C repo
    return status code
    local lang
    no print the command
    """
    return command_git_check_print(repo, params, False)


def command_git_check_print(repo, params, display):
    """
    command git -C repo
    return status code
    local lang
    if display True, print the command
    """
    params_git = ["git", "-C", repo]
    try:
        ligne_commande = params_git + params
        if display and compute_args().debug:
            print("debug : " + str(ligne_commande))
        return subprocess.check_output(ligne_commande).decode()
    except subprocess.CalledProcessError:
        return ""


def command_git_call(repo, params):
    """
    command git -C repo
    return the output
    no print the command
    local lang
    """
    command_git_call_print(repo, params, False)


def command_git_call_print(repo, params, display):
    """
    command git -C repo
    return the output
    if display True print the command
    local lang
    """
    params_git = ["git", "-C", repo]
    ligne_commande = params_git + params
    if display and compute_args().debug:
        print("debug : " + str(ligne_commande))
    subprocess.call(params_git + params)
