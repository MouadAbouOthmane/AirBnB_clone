#!/usr/bin/python3
"""Unit Test"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest

class TestFileStorage(unittest.TestCase):
    """ ### """

    def test_file_path(self):
        """ ### """
        f = FileStorage()
        self.assertEqual(f._FileStorage__file_path, 'file.json')

    def test_type_objects(self):
        """ ### """
        f = FileStorage()
        self.assertEqual(type(f.all()), dict)

    def test_all_func(self):
        """ ### """
        f = FileStorage()
        self.assertEqual(f.all(), f._FileStorage__objects)

    def test_new_func(self):
        """ ### """
        b = BaseModel()
        f = FileStorage()
        f.new(b)
        key = "BaseModel." + b.id
        self.assertEqual(f.all()[key], b)

    def test_reload(self):
        f = FileStorage()
        fd = f.all().copy()
        f.reload()
        self.assertNotEqual(f.all(), fd)


if __name__ == '__main__':
    unittest.main()
