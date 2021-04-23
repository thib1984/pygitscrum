import pkg_resources


def version_pygitscrum():
    print(
        "version pygitscrum : "
        + pkg_resources.get_distribution("pygitscrum").version
    )