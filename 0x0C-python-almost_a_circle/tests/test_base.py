"""Unit test for the base class BASE
"""
import unittest
from models.base import Base
import json
import pep8


class TestBaseClass(unittest.TestCase):
    """TestBaseClass resume

    Args:
        unittest (): Propertys for unit testing
    """
    def setUp(self):
        """Return to 0 class attributes"""
        Base._Base__nb_objects = 0

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(Base.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Base.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Base):
            self.assertTrue(len(func.__doc__) > 0)

    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base.py'
        file2 = 'tests/test_models/test_base.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

    def test_empty(self):
        """Test the base class without params
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_manual(self):
        """Test with manual entry
        """
        b1 = Base(15)
        self.assertEqual(b1.id, 15)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base(2)
        self.assertEqual(b3.id, 2)

    def test_extra_entry(self):
        """Test with manual entry
        """
        self.assertRaises(TypeError, Base, 1, 1, 1, 1, 1, 1)

    def test_mixed(self):
        """Test mixing
        """
        b5 = Base(15)
        self.assertEqual(b5.id, 15)
        b4 = Base()
        self.assertEqual(b4.id, 1)
        b3 = Base(2)
        self.assertEqual(b3.id, 2)
        b2 = Base(1)
        self.assertEqual(b2.id, 1)

    def test_dictionary_json(self):
        """Test the function that converts a dict to json
        """
        base = Base(100)
        self.assertEqual(base.to_json_string(None), "[]")
        my_dict = {}
        self.assertEqual(base.to_json_string(my_dict), "[]")
        my_dict = {"test": 5}
        self.assertEqual(base.to_json_string(my_dict), '{"test": 5}')
        self.assertEqual(type(base.to_json_string(my_dict)), str)

    def test_dictionary_json_good(self):
        """Test the function with good cases
        """
        base = Base(100)
        my_dict = {"id": 5, "x": 2}
        self.assertDictEqual(json.loads(base.to_json_string(my_dict)),
                             json.loads('{"id": 5, "x": 2}'))

    def test_json_string(self):
        """Test the function with null cases
        """
        base = Base(100)
        list_input = []
        self.assertEqual(base.from_json_string(None), [])
        self.assertEqual(base.from_json_string(list_input), [])

    def test_json_string_good(self):
        """Test the function with good cases
        """
        base = Base(100)
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        my_json = base.to_json_string(list_input)
        self.assertEqual(base.from_json_string(my_json),
                         [{'height': 4, 'width': 10, 'id': 89},
                         {'height': 7, 'width': 1, 'id': 7}])

if __name__ == '__main__':
    unittest.main()
