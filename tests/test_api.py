import json
import unittest

from api import app, common


class TestApiCalls(unittest.TestCase):
    def test_get_all_forums(self):
        tester = app.app.test_client(self)
        response = tester.get('/api/forums')
        # convert from bytes to json object
        response = json.loads(response.data)
        self.assertEqual(response['success'], True)
        self.assertIsInstance(response['forums'], list)

    def test_add_forum(self):
        tester = app.app.test_client(self)
        response = tester.post('/api/forums', data=dict(name="test", description="test"))
        # convert from bytes to json object
        response = json.loads(response.data)
        self.assertEqual(response['success'], True)
        common.remove_forum(common.get_last_id_forum())

    def test_remove_forum(self):
        tester = app.app.test_client(self)
        common.add_forum_into_file("test", "test")
        response = tester.delete('/api/forums', data={"id": common.get_last_id_forum()})
        # convert from bytes to json object
        response = json.loads(response.data)
        self.assertEqual(response['success'], True)
