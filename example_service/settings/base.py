# Base settings file. Put all default settings in here, in either single dictionary
# format if you are using plain SOA settings, or in Django format if you are
# using Django.
from __future__ import unicode_literals

settings = {
    "transport": {
        "path": "ebsoa.transport.asgi.server:ASGIServerTransport",
        # kwargs will need overriding in a concrete settings file
    },
    "serializer": {
        "path": "ebsoa.serializer.msgpack_serializer:MsgpackSerializer",
    },
    "middleware": [
        ("ebsoa.server.middleware.auth:AuthMiddleware", {})
    ],
}
