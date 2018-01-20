import conformity
import pysoa
from pysoa.test.server import ServerTestCase

import example_service
from example_service.server import Server


class TestServiceCall(ServerTestCase):
    """
    This illustrates how to test actions on the same service using the built-in
    TestCase subclass
    """

    # You need to put the server class you're testing here as a class variable
    # so the test suite can instantiate it and set it up for you.
    server_class = Server

    def test_square(self):
        """
        Tests that the "square" action correctly squares numbers.
        """
        # There's a premade client that routes to the service you passed as server_class
        response = self.call_action('square', body={'number': 2})
        self.assertEqual(4, response.body['square'])

    def test_status(self):
        """
        Tests that the "healthcheck" action works.
        """
        response = self.call_action('status')
        self.assertEqual(example_service.__version__, response.body['version'])
        self.assertEqual(conformity.__version__, response.body['conformity'])
        self.assertEqual(pysoa.__version__, response.body['pysoa'])
        self.assertEqual([], response.body['healthcheck']['errors'])
        self.assertEqual(
            [('TURBOENCABULATOR_SPACE', 'Turboencabulator has less than 5% space left')],
            response.body['healthcheck']['warnings']
        )
