#!/usr/bin/env python3
"""
Unit test for utils.access_nested_map
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch
from unittest.mock import MagicMock
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    TestCase class that will hold
    the test methods
    """
    @parameterized.expand([
        ({"a": 1}, ("a", ), 1),
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, mapp, path, expected):
        """Tests for the return of utils.access_nested_map"""
        self.assertEqual(access_nested_map(mapp, path), expected)

    @parameterized.expand([
        ({}, ("a", )),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, mapp, path):
        """Test that a KeyError is raised"""
        self.assertRaises(KeyError, access_nested_map, mapp, path)


class TestGetJson(unittest.TestCase):
    """
    TestCase class that will hold the
    test methods for utils.get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")  # Patch decorator for requests.get
    def test_get_json(self, url, payload, mock_get):
        """Tests for the return of utils.get_json"""
        mock_response = MagicMock()
        mock_response.json.return_value = payload

        mock_get.return_value = mock_response
        self.assertEqual(get_json(url), payload)
