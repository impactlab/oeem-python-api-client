import os

def auth_token():
    token = os.environ.get("DATASTORE_ACCESS_TOKEN", 'uFxwXUtDFz2a8ha2wXMxBqD7WTW623fpy7pbNpmq')
    return token 

def datastore_url():
    """Get the datastore URL
    """
    url = os.environ.get("DATASTORE_URL", "test-datastore.openeemeter.org")
    return url
    
