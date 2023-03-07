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
        for forum in response['forums']:
            self.assertIsInstance(forum, dict)
            self.assertIsInstance(forum['id'], int)
            self.assertIsInstance(forum['name'], str)
            self.assertIsInstance(forum['description'], str)

    def test_add_forum(self):
        tester = app.app.test_client(self)
        response = tester.post(
            '/api/forums', data=dict(name="test", description="test"))
        # convert from bytes to json object
        response = json.loads(response.data)
        self.assertEqual(response['success'], True)
        common.remove_forum(common.get_last_id_forum())

    def test_remove_forum(self):
        tester = app.app.test_client(self)
        last_id = common.get_last_id_forum()
        common.add_forum_into_file("test_remove_forum", "test")
        forums = json.loads(tester.get('/api/forums').data)['forums']
        self.assertEqual(forums[len(forums) - 1]['name'], "test_remove_forum")
        response = tester.delete(
            '/api/forums', data=dict(id=common.get_last_id_forum()))
        # convert from bytes to json object
        response = json.loads(response.data)
        self.assertEqual(response['success'], True)
        self.assertEqual(common.get_last_id_forum(), last_id)

    def test_insert_message(self):
        tester = app.app.test_client(self)
        message = "test_insert_message"
        response = tester.post(
            '/api/message', data=dict(nickname="test", message=message, forum=1))
        # convert from bytes to json object
        response = json.loads(response.data)
        self.assertEqual(response['success'], True)
        # getting the last message to check it is the same as the one we just inserted
        messages = json.loads(tester.get(
            '/api/message', data=dict(nb=1, forum=1)).data)['messages']
        last_message = messages[0][3]
        self.assertEqual(last_message, message)

    def test_get_messages(self):
        tester = app.app.test_client(self)
        response = tester.get('/api/message?forum=1&nb=1')
        # convert from bytes to json object
        response = json.loads(response.data)
        self.assertEqual(response['success'], True)
        self.assertIsInstance(response['messages'], list)
        print(response)
        self.assertEqual(len(response['messages']), 1)
        message = response['messages'][0]
        self.assertIsInstance(message, list)
        self.assertEqual(len(message), 6)
        self.assertEqual(message[4], 1)
