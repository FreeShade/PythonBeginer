import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def test_give_default_raise(self):
        """Тестуємо ріст соляри"""
        
        my_salary = Employee('Alex', 'Liberty', 0)
        my_salary.give_raise()
        self.assertEqual(my_salary.salary, 5000)
    
        
        
if __name__ == '__main__':
    unittest.main()