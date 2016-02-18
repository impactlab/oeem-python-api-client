from unittest import TestCase
from oeem_uploader.request import Request

class TestRequest(TestCase):
    
    @classmethod
    def setUp(self):
        self.request = Request()

    def test_get_requests_of_projects(self):
        r = self.request.get('projects')
        self.assertEqual(r.status_code, 200)
        
