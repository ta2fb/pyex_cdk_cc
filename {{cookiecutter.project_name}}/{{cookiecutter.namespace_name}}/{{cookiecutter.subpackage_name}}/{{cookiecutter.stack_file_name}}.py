"""Document file"""

from aws_cdk import core


class {{cookiecutter.stack_name}}(core.Stack):
    """Main CDK stack documentation

    This project uses the Google Style Python Docstrings

    https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    """

    def __init__(self, scope: core.Construct, id: str, stage_conf, **kwargs) -> None:
        """

        Args:
            scope: Scope
            id: Unique ID
            **kwargs: Extra keyword argument list
        """
        super().__init__(scope, id, **kwargs)

        self.conf = stage_conf

        # The code that defines your stack goes here

