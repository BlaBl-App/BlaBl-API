import sqlite3
import unittest

from api import common, manage_db


class TestFunctions(unittest.TestCase):
    def test_insert_message(self):
        self.assertEqual(manage_db.insert_message(
            "nickname", "pic", "message", 1), True)

    def test_insert_message_empty(self):
        self.assertEqual(manage_db.insert_message(
            "", "pic", "message", 1), True)

    def test_insert_message_empty2(self):
        self.assertEqual(manage_db.insert_message(
            "nickname", "", "message", 1), True)

    def test_insert_message_empty3(self):
        self.assertEqual(manage_db.insert_message(
            "nickname", "pic", "", 1), True)

    def test_select_message(self):
        # returns a tab with length 10
        self.assertEqual(len(manage_db.select_message(1, 0, 1)), 1)

    def test_select_message_empty(self):
        # returns a tab with length 0
        self.assertEqual(len(manage_db.select_message(0, 0, 1)), 0)

    def test_select_message_empty2(self):
        # returns a tab with length 0 -> forum doesn't exist
        self.assertEqual(len(manage_db.select_message(10, 0, 0)), 0)

    def test_select_message_empty3(self):
        # returns a tab with length 0
        self.assertEqual(len(manage_db.select_message(-1, 0, 100)), 0)

    def test_select_message_after_insert(self):
        # returns a tab with my message
        manage_db.insert_message("nickname", "pic", "message_test", 1)
        self.assertEqual(manage_db.select_message(
            10, 0, 1)[0][3], "message_test")

    def test_select_message_after_insert2(self):
        # returns a tab with my message
        manage_db.insert_message("nickname", "pic", "message_test", 1)
        self.assertEqual(manage_db.select_message(10, 0, 1)[0][2], "nickname")

    def test_delete_messages(self):
        common.add_forum_into_file("test_delete_messages", "test")
        new_forum_id = common.get_last_id_forum()
        manage_db.insert_message(
            "nickname", "pic", "message_test", new_forum_id)
        self.assertEqual(len(manage_db.select_message(1, 0, new_forum_id)), 1)
        common.remove_forum(new_forum_id)
        self.assertEqual(len(manage_db.select_message(1, 0, new_forum_id)), 0)
