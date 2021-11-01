"""
print scripts
"""

from termcolor import colored
from pygitscrum.args import compute_args
import colorama


def print_resume_list(list_to_print, message):
    """
    print list summary
    """
    if len(list_to_print) > 0:
        print("")
        print(
            my_colored(
                message + " : ",
                "green",
            )
        )
        print(
            my_colored(
                "\n".join(map(str, list_to_print)),
                "yellow",
            )
        )
        print(
            my_colored(
                "total : " + str(len(list_to_print)),
                "green",
            )
        )


def print_resume_map(dict_to_print, message):
    """
    print dict summary
    """
    if len(dict_to_print) > 0:
        print("")
        print(my_colored(message + " : ", "green"))
        for key in dict_to_print:
            print(
                my_colored(
                    key
                    + " --> "
                    + str(dict_to_print[key])
                    + " elements",
                    "yellow",
                )
            )
        print(
            my_colored(
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
    print(my_colored(message, "yellow"))


def print_g(message):
    """
    print green message
    """
    print(my_colored(message, "green"))


def print_r(message):
    """
    print red message
    """
    print(my_colored(message, "red"))

def my_colored(message,color):
    if compute_args().nocolor:
        return message
    return colored(message, color)       
