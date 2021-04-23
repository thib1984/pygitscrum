import argparse


def compute_args():
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
        help="check your repos one by one, fetch all, and ask you if a pull/push is available, you can also pull/push or check the differences",
    )
    my_group.add_argument(
        "-t",
        "--track",
        action="store_true",
        help="check your repos one by one, track new branches, delete inexisting branches at distant, and fetch all",
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

    args = my_parser.parse_args()
    return args
