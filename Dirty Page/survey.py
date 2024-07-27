class AnonymousSurvey:
    '''Зібрати пмитання та підготуватися для зберігання відповіді.'''
    def __init__(self, question):
        '''зберкгти питання та підготуватися до зберігання відповіді'''
        self.question = question
        self.responses = []
        
    def show_question(self):
        '''Show the question.'''
        print(self.question)
        
    def store_response(self, new_response):
        '''Save one response on question'''
        self.responses.append(new_response)
        
    def show_results(self):
        '''Show all responses.'''
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")