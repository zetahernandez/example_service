# Base settings file. Put all default settings in here, in either single dictionary format if you are using plain SOA
# settings, or in Django format if you are using Django.
SOA_SERVER_SETTINGS = {
    'transport': {
        'path': 'pysoa.common.transport.http2.server:Http2ServerTransport',
    },
    'middleware': [
        # {
        #     'path': 'acme_soa_extensions.server.middleware.auth:AuthMiddleware',
        # },
    ],
}
