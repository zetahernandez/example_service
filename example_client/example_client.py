#!/usr/bin/python3

import os
import pprint
import sys

from pysoa.client import Client
from pysoa.common.transport.redis_gateway.constants import REDIS_BACKEND_TYPE_STANDARD


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ('square', 'status'):
        print('Usage: example_client.sh [square|status] ARGS')
        exit(1)

    client = Client({
        'example': {
            'transport': {
                'path': 'pysoa.common.transport.redis_gateway.client:RedisClientTransport',
                'kwargs': {
                    'backend_type': REDIS_BACKEND_TYPE_STANDARD,
                    'backend_layer_kwargs': {
                        'hosts': [
                            (os.environ['REDIS_PORT_6379_TCP_ADDR'], int(os.environ['REDIS_PORT_6379_TCP_PORT'])),
                        ],
                    },
                },
            }
        }
    })

    if sys.argv[1] == 'square':
        if len(sys.argv) != 3:
            print('Usage: example_client.sh square [number to square]')
            exit(2)
        body = {'number': int(sys.argv[2])}
        action = 'square'
    else:
        body = {}
        action = 'status'

    print('Calling `example.{}` with request body:'.format(action))
    pprint.pprint(body)
    print()

    response = client.call_action('example', action, body=body)
    print('Response:')
    pprint.pprint(response)
