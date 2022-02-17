"""Document file"""

import aws_cdk as cdk
from constructs import Construct


class {{cookiecutter.stack_name}}(cdk.Stack):
    """Main CDK stack documentation

    This project uses the Google Style Python Docstrings

    https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    """

    def __init__(self, scope: Construct, id: str, stage_conf, **kwargs) -> None:
        """

        Args:
            scope: Scope
            id: Unique ID
            **kwargs: Extra keyword argument list
        """
        super().__init__(scope, id, **kwargs)

        self.conf = stage_conf

        # The code that defines your stack goes here
