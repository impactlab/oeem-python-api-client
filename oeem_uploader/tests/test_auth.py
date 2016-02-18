from oeem_uploader.auth import * 
from unittest import TestCase

class TestAuth(TestCase):
    def test_get_token(self):
        self.assertEqual('uFxwXUtDFz2a8ha2wXMxBqD7WTW623fpy7pbNpmq', auth_token())

    def test_get_url(self):
        self.assertEqual(datastore_url(), "test-datastore.openeemeter.org")
