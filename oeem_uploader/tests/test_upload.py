from unittest import TestCase
from oeem_uploader.request import Request
from oeem_uploader.upload import upload_record


class TestUpload(TestCase):

    @classmethod
    def setUp(self):
        self.records = [{"project_id": "4848c118-7167-4929-8979-e839a20772db",
                         "baseline_period_end": "2014-05-27",
                         "baseline_period_start": "2013-08-27",
                         "reporting_period_start": "2014-08-25",
                         "reporting_period_end": "2016-02-11",
                         "latitude": "41.26996057364848",
                         "longitude": "-95.97935449486408",
                         "zipcode": "68111",
                         "weather_station": "725500",
                         "predicted_electricity_savings": "-1558.3948758637775",
                         "predicted_natural_gas_savings": "-43.28523139881372",
                         "project_cost": "6592.515721671437"
                         }]
        self.request = Request()

    def test_upload_project(self):
        response = upload_record(self.records[0],self.request)
        resp_record_singleton = None
        for project in response.json():
            if project['project_id'] == self.records[0]['project_id']:
                resp_record_singleton = project
        self.assertEqual(resp_record_singleton['project_id']
                                            , self.records[0]['project_id'])

