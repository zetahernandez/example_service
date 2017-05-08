# Base settings file. Put all default settings in here, in either single dictionary
# format if you are using plain SOA settings, or in Django format if you are
# using Django.
from __future__ import unicode_literals

settings = {
    "transport": {
        "path": "pysoa.common.transport.asgi.server:ASGIServerTransport",
        # kwargs will need overriding in a concrete settings file, like dev.py
    },
    "serializer": {
        "path": "pysoa.common.serializer.msgpack_serializer:MsgpackSerializer",
    },
    "middleware": [
        {
            "path": "ebsoa.server.middleware.auth:AuthMiddleware",
        },
    ],
}
