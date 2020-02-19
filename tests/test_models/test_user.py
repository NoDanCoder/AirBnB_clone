#!/usr/bin/python3
""" Unittest for User class
"""

from datetime import datetime
import io
from models.base_model import BaseModel
from models.user import User
from os import path, remove
import unittest
from unittest.mock import patch


class Test_instanceUser(unittest.TestCase):

    """ Class for unittest of instance check """

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_instance(self):
        """ Checks if user is instance of base_model """
        b = User()
        self.assertTrue(isinstance(b, BaseModel))

    def test_instance_args(self):
        """ Checks if user with args is instance of base_model """
        b = User(123, "Hello", ["World"])
        self.assertTrue(isinstance(b, BaseModel))

    def test_instance_kwargs(self):
        """ Checks if user with args is instance of base_model """
        d = {"name": "Holberton"}
        b = User(**d)
        self.assertTrue(isinstance(b, BaseModel))


class Test_class_attrsUser(unittest.TestCase):

    """ Class for checking if classa attr were set correctly """

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_correct_classattr(self):
        """ Checks if class attr are present """
        b = User()
        attr = ["email", "password", "first_name", "last_name"]
        d = b.__dict__
        for i in attr:
            self.assertFalse(i in d)
            self.assertTrue(hasattr(b, i))
            self.assertEqual(getattr(b, i, False), "")

    def test_set_attr(self):
        """ Check settings instance attr and accessing class attr """
        b = User()
        attr = ["email", "password", "first_name", "last_name"]
        value = ["123@hmail.com", "password", "Larry", "Page"]
        for i, j in zip(attr, value):
            setattr(b, i, j)
        d = b.__dict__
        for i, j, in zip(attr, value):
            self.assertEqual(getattr(b, i, False), j)
        for i in attr:
            self.assertEqual(getattr(b.__class__, i, False), "")
