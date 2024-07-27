from survey import AnonymousSurvey

#Визначити запитання та створити опитуваня.
question = "What language di you first learnto speak?"
my_survey = AnonymousSurvey(question)

#Показати запитання та зберегти відповіді на нього.
my_survey.show_question()
print("Enter 'q' at any time tu quit.\n")
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_response(response)
    
#Показати результати опитування.
print("\nThank you to everyone who participatd in survey!")
my_survey.show_results()