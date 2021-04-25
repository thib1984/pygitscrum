"""
print scripts
"""

from termcolor import colored
from pygitscrum.args import compute_args


def print_resume_list(list_to_print, message):
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
    if compute_args().debug:
        print("debug : " + message)


def print_y(message):
    print(colored(message, "yellow"))


def print_g(message):
    print(colored(message, "green"))