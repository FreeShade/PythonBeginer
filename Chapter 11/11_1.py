# Місто країна
import unittest
from city_function import misto_land


class MistoTest(unittest.TestCase):
    """Тести для 'city_function.py'."""

    def test_city_land_name(self):
        """Чи працює функція з іменами типу 'Kyiv, Ukraine'?"""
        formated_name = misto_land("Kyiv", "Ukraine")
        self.assertEqual(formated_name, "Kyiv, Ukraine")


if __name__ == "__main__":
    unittest.main()
