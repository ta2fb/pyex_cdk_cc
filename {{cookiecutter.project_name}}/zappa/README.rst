*****************************
{{cookiecutter.namespace_name}}.{{cookiecutter.subpackage_name}}
*****************************

Zappa configuration for settings up {{cookiecutter.namespace_name}}.{{cookiecutter.subpackage_name}} APIs

Development
###########

1. Install python virtualenv (3.6+)
2. Run the following command to create the zappa virtualenv for this project and activate it

.. code-block:: bash

    source create_activate_virtualenv.sh

3. Install other dependencies in the virtualenv to have them included in the lambda package
4. Deploy the hello world api

.. code-block:: bash

    cd hello-world
    zappa deploy

5. Note the URL after the API deploys successfully - copy the ID (e.g., https://<api_id>.execute-api.us-east-1.amazonaws.com/dev)
6. Edit test_api.py, changing the api_id variable with the ID found in step 5
7. Make sure you have AWS credentials that have IAM access to the API gateway; change aws_profile in test_api.py if necessary
8. Install the dependencies for the test_api.py script and run it

.. note::

    Do not install the dependencies for the test_api.py in the zappa virtualenv because that will add unnecessary dependencies to the lambda deploy - use the conda environment of this project or another python environment of your choosing

.. code-block:: bash

    pip install aws_requests_auth boto3 requests
    python test_api.py

9. You should receive a message back, 'Hello, world!'
10. To test without IAM authentication to ensure security, you can either run curl with the url or try and go to the url in a browser

Useful Zappa commands (run these commands in one of the endpoint directories)
*****************************************************************************

List available commands

.. code-block:: bash

    zappa -h

Deploy API

.. code-block:: bash

    zappa deploy [stage]

Update API

.. code-block:: bash

    zappa update [stage]

Tail CloudWatch logs for debugging

.. code-block:: bash

    zappa tail [stage]

Associate certificate with API

.. code-block:: bash

    zappa certify [stage]
