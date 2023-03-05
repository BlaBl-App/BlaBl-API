import unittest

from api import common


class TestAddingForum(unittest.TestCase):
    def test_adding_forum(self):
        number = len(common.get_forums_from_file())
        self.assertEqual(common.add_forum("test", "test"), True)
        self.assertEqual(len(common.get_forums_from_file()), number + 1)
        common.remove_forum(len(common.get_forums_from_file()))

    def test_adding_forum_empty(self):
        self.assertEqual(common.add_forum("", ""), True)
        common.remove_forum(len(common.get_forums_from_file()))

    def test_get_forums_from_file(self):
        self.assertIsInstance(common.get_forums_from_file(), list)
        self.assertEqual(len(common.get_forums_from_file()), len(common.get_forums_from_file()))

    def test_get_last_id_forum(self):
        self.assertEqual(common.get_last_id_forum(), 4)
        self.assertEqual(common.get_last_id_forum(), len(common.get_forums_from_file()))

    def test_remove_forum(self):
        number = len(common.get_forums_from_file())
        self.assertEqual(common.remove_forum(common.get_last_id_forum()), True)
        self.assertEqual(len(common.get_forums_from_file()), number - 1)
