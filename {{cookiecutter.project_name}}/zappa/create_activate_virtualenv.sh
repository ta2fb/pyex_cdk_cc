#! /bin/bash

ENV_NAME='{{cookiecutter.namespace_name}}.{{cookiecutter.subpackage_name}}_zappa_venv'

if [ ! -d $ENV_NAME ]; then
    virtualenv $ENV_NAME
fi
source ${ENV_NAME}/bin/activate
pip install -r requirements.txt
