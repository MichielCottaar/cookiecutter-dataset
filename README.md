Cookiecutter template for a datalad dataset, which either runs a pipeline and/or produces images.

# Features
- Sensible setup of gitattributes and gitignore
    - set up gitattributes to include markdown files, shell scripts, and python scripts in main git repository rather than the annex
    - if setting up a pipeline will ignore any "log" directory from git altogether
    - if creating images will not add jupyter notebooks or SVG images to the annex
- If creating images, scripts are included to rerun all jupyter notebooks and python/shell scripts, export any SVG images to PNG and upload it to an obsidian vault (if defined).
- If running a pipeline, an initial "main.py" is produced using [mcot.pipe](https://pypi.org/project/mcot.pipe/).

# Usage
```shell
cookiecutter https://github.com/MichielCottaar/cookiecutter-dataset.git
```