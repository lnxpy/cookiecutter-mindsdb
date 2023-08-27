#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    """removes a file

    Args:
        filepath (str): path to file
    """
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def success(text: str) -> str:
    return f"\033[1;32m{text}\033[0m"


if __name__ == "__main__":
    REMOVE_PATHS = [
        '{% if cookiecutter.include_dependencies.lower() == "n" %} requirements.txt {% endif %}',
        '{% if cookiecutter.include_version_bumper.lower() == "n" %} .bumpversion.cfg {% endif %}',
    ]

    for path in REMOVE_PATHS:
        if path:
            remove_file(path.strip())

    print(
        "+ {handler_name} is created successfully!".format(
            handler_name=success("{{ cookiecutter.handler_name }} Handler")
        )
    )
