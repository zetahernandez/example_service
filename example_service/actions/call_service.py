from conformity import fields
from pysoa.server.action import Action


class CallServiceAction(Action):
    """
    This is an example of a simple action which chains down to call another service;
    in this case, ourselves.
    """

    response_schema = fields.Dictionary({
        'square': fields.Float(),
    })

    def run(self, request):
        """
        When an action is run, the request is validated, and then passed to you here in the run() method, where you can
        perform the business logic.
        """
        # The client, which lets us call other services, is always available on the request object if any client routing
        # settings are configured in the service settings. In this case, the service is calling itself, which can only
        # work if there are two or more server processes running.
        result = request.client.call_action('example', 'square', body={'number': 42})

        return {
            'square': result.body['square'],
        }
