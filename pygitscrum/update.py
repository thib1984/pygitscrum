import subprocess


def update_pygitscrum():
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