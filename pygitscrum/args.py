"""
pygitscrum argparse gestion
"""

import argparse
import sys


def compute_args():
    """
    check args and return them
    """
    my_parser = argparse.ArgumentParser(
        description="pygitscrum : masterize git!!!",
        epilog="""
        Full documentation at: <https://github.com/thib1984/pygitscrum>.
        Report bugs to <https://github.com/thib1984/pygitscrum/issues>.
        MIT Licence.
        Copyright (c) 2021 thib1984.
        This is free software: you are free to change and redistribute it.
        There is NO WARRANTY, to the extent permitted by law.
        Written by thib1984.""",
    )
    my_parser.add_argument(
        "-v",
        "--debug",
        action="store_true",
        help="full trace",
    )
    my_group = my_parser.add_mutually_exclusive_group(required=True)
    my_group.add_argument(
        "-d",
        "--daily",
        metavar="git_period",
        action="store",
        type=str,
        nargs="?",
        const="yesterday",
        help="list your commits since <git_period> (default : yesterday) from all branches",
    )
    my_group.add_argument(
        "-s",
        "--search",
        metavar="keyword",
        action="store",
        type=str,
        help="search in logs 'keyword' from all",
    )
    my_group.add_argument(
        "-c",
        "--check",
        action="store_true",
        help="fetch all, ask you action if a pull/push is available",
    )
    my_group.add_argument(
        "-w",
        "--wip",
        action="store_true",
        help="fetch all, print stashs, branches with push available, and number of no commit changed files ",
    )
    my_group.add_argument(
        "-p",
        "--prune",
        action="store_true",
        help="DRY RUN! : fetch all, print stash, and gone local branch",
    )
    my_group.add_argument(
        "-t",
        "--track",
        action="store_true",
        help="fetch all, track new branches, delete refs from inexisting remote, fetch all",
    )
    my_group.add_argument(
        "-V",
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

    my_parser.add_argument(
        "to_path",
        metavar="to_path",
        type=str,
        nargs="?",
        default=".",
        help="the path to scan, defaut '.'",
    )

    # if no parameter
    if len(sys.argv) == 1:
        my_parser.print_help()
        sys.exit(0)

    args = my_parser.parse_args()
    return args
