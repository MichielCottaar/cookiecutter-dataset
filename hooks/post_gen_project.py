#!/usr/bin/env python
import os
from subprocess import run

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

    dl = ["datalad"]
    top_level = run("git rev-parse --show-toplevel".split(), capture_output=True).stdout.decode().strip()
    run(dl + ["create", "-f", ".", "-d", top_level])
    run(dl + ["save", "-m", "Initial dataset setup from cookiecutter"])
    ria = os.getenv("RIA")
    run(dl + ["create-sibling-ria", "-s", "laptop", "-d", ".", ria])
    run(dl + ["create-sibling-gitlab", "--project", f"ndcn0236/{{ cookiecutter.project_name }}", "--site", "win", "--publish-depends=laptop", "--access", "ssh"])
    run(dl + ["push", "--to", "win"])
