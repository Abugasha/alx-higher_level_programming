"""Unit test for the class Rectangle
"""
import unittest
from io import StringIO
from models.rectangle import Rectangle
from unittest.mock import patch
from models.base import Base
import json
import pep8


class TestRectangleClass(unittest.TestCase):
    """TestRectangleClass resume

    Args:
        unittest (): Propertys for unit testing
    """
    def setUp(self):
        """Return to 0 class attributes"""
        Base._Base__nb_objects = 0

    """ checking for documentation """
    def test_module_doc(self):
        """ checks for module doc """
        self.assertTrue(len(Rectangle.__doc__) > 0)

    def test_class_doc(self):
        """ checks for class doc """
        self.assertTrue(len(Rectangle.__doc__) > 0)

    def test_method_docs(self):
        """ checking for method doc """
        for func in dir(Rectangle):
            self.assertTrue(len(func.__doc__) > 0)

    def test_pep8(self):
        """ test rectangle and test_rectangle
            for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/rectangle.py'
        file2 = 'tests/test_models/test_rectangle.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

    def test_invalid_value(self):
        """Test to validate zero or negative integers"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-5, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 1, -10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 1, 1, -10)

    def test_empty(self):
        """Test the base class without params
        """
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, 1)

    def test_2_params(self):
        """Test with 2 params
        """
        r1 = Rectangle(2, 4)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_4_params(self):
        """Test with 4 params
        """
        r2 = Rectangle(2, 4, 3, 1)
        self.assertEqual(r2.id, 1)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 1)

    def test_5_params(self):
        """Test with 5 params
        """
        r3 = Rectangle(2, 4, 3, 1, 50)
        self.assertEqual(r3.id, 50)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 4)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 1)

    def test_lot_params(self):
        """Test with more than 5 params
        """
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, 1, 1, 1)

    def test_type_errors(self):
        """Test with not int input
        """
        self.assertRaises(TypeError, Rectangle, "2", 2)
        self.assertRaises(TypeError, Rectangle, 2, "2")
        self.assertRaises(TypeError, Rectangle, [2], [2])
        self.assertRaises(TypeError, Rectangle, (2,), 2)
        self.assertRaises(TypeError, Rectangle, 2, {1, 2}, 5, 9)
        self.assertRaises(TypeError, Rectangle, 8, 6, 3, (1, 2))
        self.assertRaises(TypeError, Rectangle, 2.0, 2.5)
        self.assertRaises(TypeError, Rectangle, 2, 2, [2], 2)
        self.assertRaises(TypeError, Rectangle, 2, 2, 2, [2])
        self.assertRaises(TypeError, Rectangle, 2, 2, 2, [2], 2)
        self.assertRaises(TypeError, Rectangle, 2, float("inf"), 8, 1)
        self.assertRaises(TypeError, Rectangle, 2, float("nan"), 8, 1)

    def test_value_errors(self):
        """Test with 0 and negative inputs
        """
        self.assertRaises(ValueError, Rectangle, 0, 0)
        self.assertRaises(ValueError, Rectangle, -2, 2)
        self.assertRaises(ValueError, Rectangle, -2, -2)
        self.assertRaises(ValueError, Rectangle, 2, 2, 0, -2)
        self.assertRaises(ValueError, Rectangle, 2, 2, 2, -2)
        self.assertRaises(ValueError, Rectangle, 2, 2, -2, 2, 2)

    def test_area(self):
        """Test area response
        """
        r_area = Rectangle(2, 4)
        self.assertEqual(r_area.area(), 8)
        r_area = Rectangle(5, 5, 5, 5)
        self.assertEqual(r_area.area(), 25)

    def test_display_nocoords(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(2, 2)
            r1.display()
            self.assertEqual(fake_out.getvalue(), "##\n##\n")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r2 = Rectangle(1, 1)
            r2.display()
            self.assertEqual(fake_out.getvalue(), "#\n")

    def test_str_response(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(2, 2)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (1) 0/0 - 2/2\n")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(4, 6, 2, 1, 12)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (12) 2/1 - 4/6\n")

    def test_display_coords(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(2, 2, 1, 1)
            r1.display()
            self.assertEqual(fake_out.getvalue(), "\n ##\n ##\n")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r2 = Rectangle(1, 1, 4, 4)
            r2.display()
            self.assertEqual(fake_out.getvalue(), "\n\n\n\n    #\n")

    def test_update_1_value(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(4)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 10/10 - 10/10\n")

    def test_update_2_values(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(4, 20)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 10/10 - 20/10\n")

    def test_update_3_values(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(4, 20, 5)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 10/10 - 20/5\n")

    def test_update_4_values(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(4, 20, 5, 1)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 1/10 - 20/5\n")

    def test_update_5_values(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(4, 20, 5, 1, 6)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 1/6 - 20/5\n")

    def test_update_empty(self):
        """Test update empty
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update()
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (1) 10/10 - 10/10\n")

    def test_update_typerrors(self):
        """Test update empty
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertRaises(TypeError, r1.update, 1, [1])
        self.assertRaises(TypeError, r1.update, 1, 2, "4")
        self.assertRaises(TypeError, r1.update, 1, 2, 3, "4")
        self.assertRaises(TypeError, r1.update, 1, 2, 3, 4, "5")

    def test_update_valerrors(self):
        """Test update bad inputs
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertRaises(ValueError, r1.update, 1, 0)
        self.assertRaises(ValueError, r1.update, 1, 0)
        self.assertRaises(ValueError, r1.update, 1, 1, -1)
        self.assertRaises(ValueError, r1.update, 1, 1, 1, -1)

    def test_update_k1_value(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(id=4)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 10/10 - 10/10\n")

    def test_update_k2_values(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(id=4, width=20)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 10/10 - 20/10\n")

    def test_update_k3_values(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(id=4, width=20, height=5)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 10/10 - 20/5\n")

    def test_update_k4_values(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(id=4, width=20, height=5, x=1)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 1/10 - 20/5\n")

    def test_update_k5_values(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(id=4, width=20, height=5, x=1, y=6)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 1/6 - 20/5\n")

    def test_update_args_prio(self):
        """Test updates
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(5, id=4, width=20, height=5, x=1, y=6)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (5) 10/10 - 10/10\n")

    def test_cmp_dict(self):
        """Test compare dict return value
        """
        r1 = Rectangle(10, 10, 10, 10, 10)
        good_answer = {"id": 10, "width": 10, "height": 10, "x": 10, "y": 10}
        self.assertEqual(r1.to_dictionary(), good_answer)

    def test_cmp_dict2(self):
        """Test compare dict return value
        """
        r1 = Rectangle(10, 10, 0, 0, 5)
        good_answer = {"id": 5, "width": 10, "height": 10, "x": 0, "y": 0}
        self.assertEqual(r1.to_dictionary(), good_answer)

    def test_create(self):
        """Creates an instance with a dict
        """
        base = Rectangle(1, 1)
        first_ins = {'id': 89, 'width': 10, 'height': 4, "x": 1, "y": 1}
        my_rect = base.create(**first_ins)
        self.assertEqual(my_rect.id, 89)
        self.assertEqual(my_rect.width, 10)
        self.assertEqual(my_rect.height, 4)
        self.assertEqual(my_rect.x, 1)
        self.assertEqual(my_rect.y, 1)

    def test_dictionary_json(self):
        """Test the function that converts a dict to json
        """
        base = Rectangle(1, 1)
        self.assertEqual(base.to_json_string(None), "[]")
        my_dict = {}
        self.assertEqual(base.to_json_string(my_dict), "[]")
        my_dict = {"test": 5}
        self.assertEqual(base.to_json_string(my_dict), '{"test": 5}')
        self.assertEqual(type(base.to_json_string(my_dict)), str)

    def test_dictionary_json_good(self):
        """Test the function with good cases
        """
        base = Rectangle(1, 1)
        my_dict = {"id": 5, "x": 2}
        self.assertDictEqual(json.loads(base.to_json_string(my_dict)),
                             json.loads('{"id": 5, "x": 2}'))

    def test_json_string(self):
        """Test the function with null cases
        """
        base = Rectangle(1, 1)
        list_input = []
        self.assertEqual(base.from_json_string(None), [])
        self.assertEqual(base.from_json_string(list_input), [])

    def test_json_string_good(self):
        """Test the function with good cases
        """
        base = Rectangle(1, 1)
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
