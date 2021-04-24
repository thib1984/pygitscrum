"""
--update scripts
"""

import subprocess
from shutil import which


def update_pygitscrum():
    """
    entry point for --update
    """
    prog = "pip3"
    if (which("pip3")) is None:
        prog = "pip"
    params = [
        prog,
        "install",
        "--upgrade",
        "pygitscrum",
    ]
    subprocess.check_call(params)
