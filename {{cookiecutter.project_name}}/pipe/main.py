"""
Runs the main pipeline
"""
from mcot.pipe.pipeline import pipe
from mcot.pipe.datalad import get_tree
tree = get_tree('.')

# add jobs to the pipeline


if __name__ == "__main__":
    pipe.cli(tree)