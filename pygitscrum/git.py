"""
git general scripts
"""
import os
import subprocess
from pygitscrum.args import compute_args
from pygitscrum.print import print_debug


def git_code(repo, params):
    params_git = ["git", "-C", repo]
    ligne_commande = params_git + params
    try:
        print_debug("debug : " + str(ligne_commande))
        return subprocess.check_call(
            ligne_commande,
        )
    except Exception:
        return 1


def git_code_silent(repo, params):
    new_env = dict(os.environ)
    new_env["LC_ALL"] = "EN"
    params_git = ["git", "-C", repo]
    ligne_commande = params_git + params
    try:
        print_debug("debug : " + str(ligne_commande))
        return subprocess.check_call(
            ligne_commande,
            stderr=subprocess.STDOUT,
            stdout=subprocess.DEVNULL,
            env=new_env,
        )
    except Exception as err:
        print_debug(" /!\ error /!\ : " + str(err))
        return 1


def git_output(repo, params):
    new_env = dict(os.environ)
    new_env["LC_ALL"] = "EN"
    params_git = ["git", "-C", repo]
    ligne_commande = params_git + params
    try:
        print_debug("debug : " + str(ligne_commande))
        subprocess.check_call(
            ligne_commande,
            stderr=subprocess.STDOUT,
            stdout=subprocess.DEVNULL,
            env=new_env,
        )
        return subprocess.check_output(
            ligne_commande,
            env=new_env,
        ).decode("utf-8")
    except Exception:
        if compute_args().debug:
            subprocess.call(params_git + params, env=new_env)
        return ""
