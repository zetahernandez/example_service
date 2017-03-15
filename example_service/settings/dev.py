# Development overrides go in a file like this. While it technically mutates
# the dict in the other file too, settings files are only loaded if they are
# used, so it's fine.
from __future__ import unicode_literals
from ebsoa.transport.asgi.constants import ASGI_CHANNEL_TYPE_REDIS
from .base import settings


settings['transport']['kwargs'] = {
    "asgi_channel_type": ASGI_CHANNEL_TYPE_REDIS,
    "asgi_channel_redis_host": "localhost",
    "asgi_channel_redis_port": 6379,
}
