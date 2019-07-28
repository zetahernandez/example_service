#!/usr/bin/python3

import json
import os
import sys
import concurrent

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
                    'backed_layer_kwargs': {
                        'http_host': '127.0.0.1',
                        'http_port': '8080',
                    }
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

    def run_client():
        response = client.call_action('example', action, body=body)
        print('Response:')
        print(json.dumps(attr.asdict(response), indent=4, sort_keys=True))

    def run_parallel():
        action_responses = client.call_actions_parallel('example', [
            {'action': 'square', 'body': {'number': 1}},
            {'action': 'square', 'body': {'number': 2}},
            {'action': 'square', 'body': {'number': 3}},
            {'action': 'square', 'body': {'number': 4}},
            {'action': 'square', 'body': {'number': 5}},
            {'action': 'square', 'body': {'number': 6}},
            {'action': 'square', 'body': {'number': 7}},
            {'action': 'square', 'body': {'number': 8}},
            {'action': 'square', 'body': {'number': 9}},
        ])
        print(list(action_responses))

    import multiprocessing as mp

    # Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(mp.cpu_count())

    results = [pool.apply(run_parallel) for _ in range(1000)]

    pool.close()
    run_client()
    run_parallel()
