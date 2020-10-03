from setuptools import find_packages, setup

setup(
    name="lgtm",
    version="1.0.0",
    package=find_packages(exclude=("tests", "outputs", "sub_workplace")),
    install_requires=[
        "Click~=7.1.2",
        "Pillow~=6.2.2",
        "requests~=2.22.0"
    ],
    entry_points={
        "console_scripts": [
            "lgtm=lgtm.core:cli"
        ]
    }
)