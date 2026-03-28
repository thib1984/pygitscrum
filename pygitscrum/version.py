"""
--version scripts
"""

from importlib.metadata import version

def version_pygitscrum():
    """
    entry point for --version
    """
    print(
        "version pygitscrum : "
        + version("pygitscrum")
    )
