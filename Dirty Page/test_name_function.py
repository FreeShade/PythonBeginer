import unittest
from name_function import get_formated_name


class NamesTestCase(unittest.TestCase):
    """Тести для 'name_function.py'."""

    def test_first_last_name(self):
        """Чи працює з іменами на кшталт 'Janis Joplin'?"""
        formated_name = get_formated_name("janis", "joplin")
        self.assertEqual(formated_name, "Janis Joplin")

    def test_first_last_middle_name(self):
        """Чи працює з іменами на кшталт 'Wolfgang Amadeus Mozart'?"""
        formated_name = get_formated_name("wolfgang", "mozart", "amadeus")
        self.assertEqual(formated_name, "Wolfgang Amadeus Mozart")


if __name__ == "__main__":
    unittest.main()
