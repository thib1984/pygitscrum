"""
pygitscrum init
"""

from pygitscrum.args import compute_args
from pygitscrum.scan import scan_directories
from pygitscrum.update import update_pygitscrum
from pygitscrum.version import version_pygitscrum
from pygitscrum.git_search import git_search
from pygitscrum.git_check import git_check
from pygitscrum.git_daily import git_daily
from pygitscrum.git_track import git_track
from pygitscrum.git_wip import git_wip
from pygitscrum.git_prune import git_prune
from pygitscrum.git_fetch import git_fetch
from pygitscrum.git_show import git_show


def pygitscrum():
    """
    pygitscrum entry point
    """
    args = compute_args()

    if args.version:
        version_pygitscrum()
    elif args.update:
        update_pygitscrum()
    elif args.track:
        git_track(scan_directories())
    elif args.fetch:
        git_fetch(scan_directories())
    elif args.check:
        git_check(scan_directories())
    elif args.daily:
        git_daily(scan_directories())
    elif args.search:
        git_search(scan_directories())
    elif args.show:
        git_show(scan_directories())
    elif args.wip:
        git_wip(scan_directories())
    elif args.prune:
        git_prune(scan_directories())
