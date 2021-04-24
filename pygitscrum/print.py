"""
print scripts
"""

from termcolor import colored


def print_resume(list_to_print, message):
    """
    print list summary
    """
    if len(list_to_print) > 0:
        print("")
        print(
            colored(
                message + " : ",
                "green",
            )
        )
        print(
            colored(
                "\n".join(map(str, list_to_print)),
                "yellow",
            )
        )