class Employee:
    '''
    Збирає відомості про працівника.
    '''
    def __init__(self, name, second_name, salary):
        '''Зберегти та параметри'''
        self.name = name
        self.second_name = second_name
        self.salary = salary
        
        
    def give_raise(self):
        '''Додає 5000 до соляри'''
        self.salary = self.salary + 5000
        
    def show_full(self):
        '''
        Показати інфу по співробітнику.
        '''
        full_name = f"{self.name} {self.second_name}"
        print(f'{full_name} His salary is {self.salary}')