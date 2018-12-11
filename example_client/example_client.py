#!/usr/bin/python3

import json
import os
import sys

import attr
from pysoa.client import Client
from pysoa.common.transport.redis_gateway.constants import REDIS_BACKEND_TYPE_STANDARD


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ('call_service', 'square', 'status'):
        print('Usage: example_client.sh [square|status] ARGS')
        exit(1)

    client = Client({
        'example': {
            'transport': {
                'path': 'pysoa.common.transport.http2.client:Http2ClientTransport',
                'kwargs': {
                    'http_host': '127.0.0.1',
                    'http_port': '8080',
                },
            }
        }
    })

    if sys.argv[1] == 'call_service':
        body = {}
        action = 'call_service'
    elif sys.argv[1] == 'square':
        if len(sys.argv) != 3:
            print('Usage: example_client.sh square [number to square]')
            exit(2)
        body = {'number': int(sys.argv[2])}
        action = 'square'
    else:
        body = {}
        action = 'status'

    print('Calling `example.{}` with request body:'.format(action))
    print(json.dumps(body, indent=4, sort_keys=True))
    print()

    response = client.call_action('example', action, body=body)
    print('Response:')
    print(json.dumps(attr.asdict(response), indent=4, sort_keys=True))
