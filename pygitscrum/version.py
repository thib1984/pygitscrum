"""
--version scripts
"""

import pkg_resources


def version_pygitscrum():
    """
    entry point for --version
    """
    print(
        "version pygitscrum : "
        + pkg_resources.get_distribution("pygitscrum").version
    )
