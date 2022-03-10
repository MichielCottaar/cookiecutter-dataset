#!/usr/bin/env sh
datalad get notebooks
datalad unlock notebooks

for fn in $(find notebooks -not -path '*/\.*' -name '*.ipynb' ! -name movie.ipynb) ; do
    jupyter nbconvert --to notebook --inplace --execute --ExecutePreprocessor.timeout=600 --allow-errors $fn &
done

for fn in $(find notebooks -not -path '*/\.*' -name '*.py') ; do
    echo running $fn
    python $fn &
done

for fn in $(find notebooks -not -path '*/\.*' -name '*.sh') ; do
    echo running $fn
    bash $fn &
done

wait

inkscape/export.sh
