from pysoa.server import server

# Import each action explicitly; don't use "import *". Try to keep each action in its own Python module or in small
# modules with related actions; don't just have one big actions.py file.
from example_service.actions.call_service import CallServiceAction
from example_service.actions.square import SquareAction
from example_service.actions.status import StatusAction


class Server(server.Server):
    """
    The main server class for this service.

    The server class handles registering Action names to their corresponding
    Action classes, and the superclass contains all the logic necessary for
    running and serving requests, meaning all you need to do is call the
    class method Server.main() to run the service.

    This main method also handles command line argument parsing and loading
    settings.
    """

    # The service name is required, and is what the transport classes will use
    # (if necessary) to know what named requests they should pick up.
    service_name = 'example'

    # This maps action names (keys) to action class objects (values). You are
    # required to have a "healthcheck" action at a minimum; see the
    # example HealthcheckAction for information on how that should behave.
    # Everything else is up to you; try to keep names short but explicit, and
    # don't end them in redundant terms like "echo_action"
    action_class_map = {
        'status': StatusAction,
        'call_service': CallServiceAction,
        'square': SquareAction,
    }

    def setup(self):
        """
        If you want to perform loads or initialisation on service boot,
        then put that in a setup() method, which will be called just before
        the service starts taking requests. It's better here than in a module
        body or __init__ override as this won't get called if you're just being
        imported or introspected.
        """
        pass
