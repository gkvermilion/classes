import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Japanese', 'Spanish']


    def test_store_single_response(self):
        """проверяет, что один ответ сохранен правильно"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)


    def test_store_three_response(self):
        """проверяет, что три ответа были сохранены правильно"""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
