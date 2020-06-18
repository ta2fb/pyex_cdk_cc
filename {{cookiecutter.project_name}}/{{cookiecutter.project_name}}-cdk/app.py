#!/usr/bin/env python3

from aws_cdk import core

from {{cookiecutter.namespace_name}}.{{cookiecutter.subpackage_name}}.{{cookiecutter.stack_file_name}} import {{cookiecutter.stack_name}}


app = core.App()
{{cookiecutter.stack_name}}(app, "{{cookiecutter.project_name}}")

app.synth()
