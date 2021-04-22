from setuptools import setup


setup(
    name="pygitscrum",
    version="0.0.3",
    description="pygitscrum",
    long_description="The complete description/installation/use/FAQ is available at : https://github.com/thib1984/pygitscrum#readme",
    url="https://github.com/thib1984/pygitscrum",
    author="thib1984",
    author_email="thibault.garcon@gmail.com",
    license="MIT",
    packages=["pygitscrum"],
    install_requires=["termcolor"],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "pygitscrum=pygitscrum.__init__:pygitscrum"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
