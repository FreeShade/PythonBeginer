import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''Тестм для класу AnonymousSurvey'''


    def setUp(self):
        '''
        Cтворити опитування та набір відповідей
        для всіх тестувальних методів.
        '''
        question = "What language did you first learn to speak ?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Ukrainian', 'Python']
        

    def test_store_single_response(self):
        '''Перевірити, чи одиночна відповідь зберігається правильно.'''
        #question = "What language did you first learn to speak?"
        #my_survey = AnonymousSurvey(question)
        #my_survey.store_response('English')
        #self.assertIn('English', my_survey.responses)
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        
        
    def test_store_three_responses(self):
        """
        Перевірити, чи три індивідуальних
        відповіді зберігаються правильно.
        """
     
        #question = 'What language did you first learn to speak'
        #my_survey = AnonymousSurvey(question)
        #responses = ['English', 'Spanish', 'Ukrainian', 'Mandarin']
        for response in self.responses:
            self.my_survey.store_response(response)
            
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
        
if __name__ == '__main__':
    unittest.main()