import unittest
from name_function import get_formated_name


class NamesTestCase(unittest.TestCase):
    """Тести для 'name_function.py'."""

    def test_first_last_name(self):
        """Чи працює з іменами на кшталт 'Janis Joplin'?"""
        formated_name = get_formated_name("janis", "joplin")
        self.assertEqual(formated_name, "Janis Joplin")


if __name__ == "__main__":
    unittest.main()
