from __future__ import unicode_literals
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
        When an action is run, the request is validated, and then passed to you
        here in the run() method, where you can perform the business logic.
        """
        # The client router, which lets us get clients for other services, is
        # always available on the request object
        client = request.client_router.get_client("example")
        result = client.call_action("square", body={"number": 42})
        # Return the result
        return {
            "square": result.body['square'],
        }
