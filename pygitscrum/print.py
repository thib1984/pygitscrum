"""
print scripts
"""

from termcolor import colored
from pygitscrum.args import compute_args
import colorama


def print_resume_list(list_to_print, message):
    colorama.init()
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
        print(
            colored(
                "total : " + str(len(list_to_print)),
                "green",
            )
        )


def print_resume_map(dict_to_print, message):
    """
    print dict summary
    """
    colorama.init()
    if len(dict_to_print) > 0:
        print("")
        print(colored(message + " : ", "green"))
        for key in dict_to_print:
            print(
                colored(
                    key
                    + " --> "
                    + str(dict_to_print[key])
                    + " elements",
                    "yellow",
                )
            )
        print(
            colored(
                "total : "
                + str(len(dict_to_print))
                + " --> "
                + str(sum(dict_to_print.values()))
                + " elements ",
                "green",
            )
        )


def print_debug(message):
    """
    print debug message
    """
    if compute_args().debug:
        print("debug : " + message)


def print_y(message):
    """
    print yellow message
    """
    colorama.init()
    print(colored(message, "yellow"))


def print_g(message):
    """
    print green message
    """
    colorama.init()
    print(colored(message, "green"))


def print_r(message):
    """
    print red message
    """
    colorama.init()
    print(colored(message, "red"))
