# Development overrides go in a file like this. While it technically mutates the dict in the other file too, settings
# files are only loaded if they are used, so it's fine.
import os

from pysoa.common.transport.redis_gateway.constants import REDIS_BACKEND_TYPE_STANDARD

from example_service.settings.base import SOA_SERVER_SETTINGS


SOA_SERVER_SETTINGS['transport']['kwargs'] = {
    'backed_layer_kwargs': {
        'http_host': '127.0.0.1',
        'http_port': '8080',
    }
}

# Services don't actually know how to talk to anything else - even themselves - so we have to set the client routing to
# enable that. Normally you would configure a service to talk to other services, not to itself, but this example works.
SOA_SERVER_SETTINGS['client_routing'] = {
    'example': {
        'transport': {
            'path': 'pysoa.common.transport.http2.client:Http2ClientTransport',
            'kwargs': SOA_SERVER_SETTINGS['transport']['kwargs'],
        },
    },
}
