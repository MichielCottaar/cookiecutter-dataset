This dataset contains:
- input datasets in `input_data`
{% if cookiecutter.include_pipeline == "y" -%}
- processed data from the pipeline in `derivatives`
{% endif -%}
{%if cookiecutter.include_figures == "y" -%}
- notebooks for generating figures in `notebooks`. These images are stored in `notebooks` directory itself or in `raw`.
- SVG images created by inkscape in `inkscape`. These images combine the figures produced by the notebooks into publication-ready figures.
- PNG versions of the SVG images in `final`. Any SVG images in the `raw` or `inkscape` directories are exported into the `final` directory.
{%- endif%}

The data is managed through [datalad](https://www.datalad.org/). This means most files will be stored in the git annex rather than the main git repository. To access those files use `datalad get <filename>`. The following files are stored in the git repository directly:
- Markdown files (*.md)
- Python scripts (*.py)
- Shell scripts (*.sh)
{%if cookiecutter.include_figures == "y" -%}
- Jupyter notebooks (*.ipynb)
- SVG images (*.ipynb)
{%- endif%}

{%if cookiecutter.include_pipeline == "y" -%}
# Running the pipeline
The main pipeline can be run using `pipe/main.py`. Run `pipe/main.py --help` for more information.
{%- endif%}

{%if cookiecutter.include_figures == "y" -%}
# Generating figures
Images are created by running one of three scripts. Each script will call the next one in the sequence:
- `pipe/generate.sh`: executes all the notebooks and python scripts. Running this will require access to a lot of the underlying data. Note that notebooks are run from the directory they are in, while python scripts are run from the top-level directory. Output SVG images can be stored locally or in the `raw` directory.
- `pipe/convert.sh`: exports the SVG files in `inkscape` and `notebooks` as PNGs in `final`. This script should be able to run without direct access to the {{cookiecutter.project_name}} data.
- `pipe/to_vault.sh`: copies the PNG output to my Obsidian vault of notes. All images will be copied to "${VAULT}/attachments/{{cookiecutter.project_name}}" and prepended with "{{cookiecutter.project_name}}".
{%- endif %}

All scripts are expected to run from the top-level directory.
