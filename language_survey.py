from survey import AnonymousSurvey

# определение вопроса с созданием экземпляра класса
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# вывод вопроса и сохранение ответов
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# вывод результатов опроса
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()