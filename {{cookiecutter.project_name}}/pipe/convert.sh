#!/usr/bin/env sh
additional_files=""

datalad unlock final

for fn in $(find inkscape/ -name *.svg) $(find raw/ -name *.svg) ; do
    datalad get $fn
    bn=`basename $fn .svg`
    for ext in png ; do
        inkscape -o final/${bn}.${ext} -b white -y 1 --export-area-drawing ${fn} &
    done
done

wait

final/to_vault.sh