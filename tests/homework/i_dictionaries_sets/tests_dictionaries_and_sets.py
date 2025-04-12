#

import unittest
from src.homework.i_dictionaries_sets import dictionary

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        dictionary.add_inventory("Widget1", 10)
        self.assertEqual(dictionary.inventory["Widget1"], 10)

        dictionary.add_inventory("Widget1", 25)
        self.assertEqual(dictionary.inventory["Widget1"], 35)

        dictionary.add_inventory("Widget1", -10)
        self.assertEqual(dictionary.inventory["Widget1"], 25)

    def test_remove_inventory_widget(self):
        dictionary.add_inventory("Widget1", 10)
        dictionary.add_inventory("Widget2", 20)

        removed = dictionary.remove_inventory_widget("Widget1")
        self.assertTrue(removed)
        self.assertEqual(len(dictionary.inventory), 1)
        self.assertIn("Widget2", dictionary.inventory)