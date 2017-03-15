from pysoa.server.action import Action
from pysoa.server.types import ActionResponse


class HealthcheckAction(Action):
    """
    A Healthcheck action is something every service must have, and it reports
    on the health of the service and its connectivity. It takes no arguments,
    and returns a response containing zero or more "errors" and "warnings".
    Zero errors and warnings means that the service is healthy; one or more
    warnings is cause for concern, and one or more errors means it is actively
    broken.

    Errors and warnings are pairs of "error code" strings with human-readable strings,
    like ("LOW_SPACE", "Storage has less than 5% disk space remaining").
    """

    # Structure all your health checks as separate methods for readability
    def check_turboencabulator(self):
        """
        Tests that we have a valid session to the turboencabulator.
        """
        return True

    def run(self, request):
        """
        This should return a response with two fields - errors, and warnings.
        """
        errors = []
        warnings = []

        # We do each check and append, rather than raising exceptions or
        # ActionErrors, so that the healthcheck returns all current warnings
        # and errors rather than just the first.
        if not self.check_turboencabulator():
            errors.append(('TURBOENCABULATOR_FAILURE', 'Cannot connect to turboencabulator'))

        return ActionResponse(body={
            'errors': errors,
            'warnings': warnings,
        })
