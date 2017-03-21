from conformity import fields
from pysoa.server.action import Action
from pysoa.server.types import ActionResponse


class SquareAction(Action):
    """
    This is an example of a simple action which takes a single input argument -
    a number to square - and returns the square of it.
    """

    # The SOA library enables validation of both requests and responses using
    # the "conformity" library. Simple schemas can be specified inline like this;
    # more complex ones should live in a separate schemas/ package (see other examples)
    request_schema = fields.Dictionary({
        # Request bodies are always dictionaries. Here we say we want a dict with exactly
        # one input - a float called "number"
        'number': fields.Float(),
    })

    response_schema = fields.Dictionary({
        'square': fields.Float(),
    })

    def run(self, request):
        """
        When an action is run, the request is validated, and then passed to you
        here in the run() method, where you can perform the business logic.
        """
        # Request body is a dictionary, so it's easy to pull out fields.
        square = request.body['number'] ** 2
        # Return the result
        return {
            "square": square,
        }
