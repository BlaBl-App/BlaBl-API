import unittest

from api import manage_db


class TestFunctions(unittest.TestCase):
    def test_insert_message(self):
        self.assertEqual(manage_db.insert_message("nickname", "pic", "message", 1), True)

    def test_insert_message_empty(self):
        self.assertEqual(manage_db.insert_message("", "pic", "message", 1), True)

    def test_insert_message_empty2(self):
        self.assertEqual(manage_db.insert_message("nickname", "", "message", 1), True)

    def test_insert_message_empty3(self):
        self.assertEqual(manage_db.insert_message("nickname", "pic", "", 1), True)

    def test_insert_message_empty4(self):
        # forum has to be an int
        self.assertEqual(manage_db.insert_message("nickname", "pic", "message", ""), False)

    def test_select_message(self):
        self.assertEqual(manage_db.select_message(10, 0, 1), [])

