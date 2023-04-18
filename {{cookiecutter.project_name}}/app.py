#!/usr/bin/env python3
import os

import aws_cdk as cdk

from {{cookiecutter.namespace_name}}.{{cookiecutter.subpackage_name}}.{{cookiecutter.stack_file_name}} import {{cookiecutter.stack_name}}


app = cdk.App()

deployment_stage = os.environ.get('DEPLOYMENT_STAGE', 'dev')
stage_conf = app.node.try_get_context(deployment_stage)

env = cdk.Environment(account=stage_conf['account_id'], region=stage_conf['region'])

{{cookiecutter.stack_name}}(app, "{{cookiecutter.project_name}}", stage_conf=stage_conf, env=env)

app.synth()
