# Response values here must be unicode strings, so if you are not using Python 3, be sure to include:
# from __future__ import absolute_import, unicode_literals
from pysoa.server.action.status import BaseStatusAction

import example_service


class StatusAction(BaseStatusAction):
    """
    A status/healthcheck action is something every service must have, and it reports on the health of the service and
    its connectivity. It takes no arguments, and returns a response containing zero or more "errors" and "warnings".
    Zero errors and warnings means that the service is healthy; one or more warnings is cause for concern, and one or
    more errors means it is actively broken.

    The base class handles the main logic for you - you just need to supply a `_version` property or attribute and zero
    or more `check_*` methods. It will find anything beginning `check_` and call it, expecting you to return either:
        - None or [], if there are no issues
        - A list of (is_error, code, description) tuples for each problem found

    `is_error` should be `True` if it's a critical error, `False` if it's just a warning.

    `code` and `description` are pairs of "error code" strings with human-readable strings, such as:

        ("LOW_SPACE", "Storage has less than 5% disk space remaining").
    """

    _version = example_service.__version__

    # Structure all your health checks as separate methods for readability
    def check_turboencabulator(self):
        """
        Tests that we have a valid session to the turboencabulator.
        """
        return [(False, 'TURBOENCABULATOR_SPACE', 'Turboencabulator has less than 5% space left')]
