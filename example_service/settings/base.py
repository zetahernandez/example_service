# Base settings file. Put all default settings in here, in either single dictionary format if you are using plain SOA
# settings, or in Django format if you are using Django.
SOA_SERVER_SETTINGS = {
    'transport': {
        'path': 'pysoa.common.transport.redis_gateway.server:RedisServerTransport',
        # kwargs will need overriding in a concrete settings file, like dev.py
    },
    'middleware': [
        # {
        #     'path': 'ebsoa.server.middleware.auth:AuthMiddleware',
        # },
    ],
}
