# Місто країна населення
import unittest
from city_function import misto_land


class MistoTest(unittest.TestCase):
    """Тести для 'city_function.py'."""

    def test_city_land_name(self):
        """Чи працює функція з іменами типу 'Kyiv, Ukraine'?"""
        formated_name = misto_land("Kyiv", "Ukraine")
        self.assertEqual(formated_name, "Kyiv, Ukraine")

    def test_city_land_poppulation_name(self):
        """Чи працює з популяцією."""
        formated_name = misto_land("Kyiv", "Ukraine", "4000")
        self.assertEqual(formated_name, "Kyiv, Ukraine, 4000")


if __name__ == "__main__":
    unittest.main()
