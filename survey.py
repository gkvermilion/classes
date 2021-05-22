class AnonymousSurvey():
    """сбор анонимных ответов на вопросы"""

    def __init__(self, question):
        """сохраняет вопрос и готовится к сохранению ответов"""
        self.question = question
        self.responses = []

    def show_question(self):
        """выводит вопрос"""
        print(self.question)

    def store_response(self, new_response):
        """сохраняет один ответ на опрос"""
        self.responses.append(new_response)

    def show_results(self):
        """выводит полученные ответы"""
        print("Survey results: ")
        for response in self.responses:
            print('- ' + response)