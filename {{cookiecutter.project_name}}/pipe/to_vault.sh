#!/usr/bin/env sh
if [ -z ${VAULT} ] && [ -d ${VAULT} ] ; then
    datalad get final

    target_dir=${VAULT}/attachments/{{cookiecutter.project_name}}
    mkdir -p ${target_dir}
    rm ${target_dir}/*.png
    for fn in final/*.png ; do
        bn=`basename ${fn}`
        cp ${fn} ${target_dir}/{{cookiecutter.project_name}}_${bn}
        chmod u+w ${target_dir}/{{cookiecutter.project_name}}_${bn}
    done
fi