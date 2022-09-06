#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":
    if "{{ cookiecutter.include_figures }}" == "n":
        for directory in ('final', 'inkscape', 'notebooks'):
            remove_file(os.path.join(directory, 'README.md'))
            os.rmdir(os.path.join(PROJECT_DIRECTORY, directory))
        remove_file('pipe/convert.sh')
        remove_file('pipe/generate.sh')
        remove_file('pipe/to_vault.sh')
    if "{{ cookiecutter.include_pipeline }}" == "n":
        remove_file('pipe/main.py')
