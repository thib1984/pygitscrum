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
from pygitscrum.args import compute_args
from pygitscrum.scan import scan_directories
from pygitscrum.update import update_pygitscrum
from pygitscrum.version import version_pygitscrum
from pygitscrum.gt_search import git_search
from pygitscrum.git_check import git_check
from pygitscrum.git_daily import git_daily
from pygitscrum.git_track import git_track


def pygitscrum():

    args = compute_args()

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
        git_daily(files)
    elif args.search:
        git_search(files)
