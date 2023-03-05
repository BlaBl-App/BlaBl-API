import sqlite3
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

    def test_select_message(self):
        # returns a tab with length 10
        self.assertEqual(len(manage_db.select_message(10, 0, 1)), 10)

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
        print(manage_db.select_message(10, 0, 1))
        self.assertEqual(manage_db.select_message(10, 0, 1)[-1][3], "message_test")

