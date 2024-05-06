


class Employee:
    '''
    Збирає відомості про працівника.
    '''
    def __init__(self, name, second_name, salary):
        '''Зберегти та параметри'''
        self.name = name
        self.second_name = second_name
        self.salary = salary
        self.full_name = f'{name} {second_name} ${salary}'
        
    def show_full_name(self):
        '''Show full fuck'''
        print(self.full_name)        
        
    def give_raise(self):
        '''Додає 5000 до соляри'''
        self.salary = self.salary + 5000
        self.full_name = f'{self.name} {self.second_name} ${self.salary}'
        
   # def store_responce(self, new_salary):
      #  self.salary.append(new_salary)
        