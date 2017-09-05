from __future__ import unicode_literals

from pysoa.test.server import ServerTestCase

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
        response = self.client.call_action('square', body={'number': 2})
        self.assertEqual(response.body['square'], 4)
