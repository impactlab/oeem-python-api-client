import requests
from .auth import auth_token, datastore_url

class Request:
    def __init__(self):
        self.token = auth_token()
        self.headers = {'Authorization': "Bearer " + self.token}
        self.url = datastore_url()

    def get(self, resource): 
        """Makes a get request to the resource
        """
        r = requests.get('http://' + self.url + '/api/v1/'+ resource, headers=self.headers)
        return r 
