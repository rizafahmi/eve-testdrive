# MONGO_HOST = 'localhost'
# MONGO_PORT = 27017
# MONGO_DBNAME = 'evetest'
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DBNAME = 0

DOMAIN = {
    'people': {
        'schema': {
            'firstname': {
                'type': 'string'
            }
        }
    }
}

RESOURCE_METHODS = ['GET', 'POST']
