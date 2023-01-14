import unittest
from survey import AnonymousSurvey
class TestAnonmyoussSurvey(unittest.TestCase):
    """ТЕсты для класса AnonymousSurvey"""

    def setUp(self) -> None:
        """"Создание опроса и набора ответов ддля всех тестовых методов"""
        question = "What"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["English", "Spanish", "Mandarine"]

    def test_store_single_response(self):
        """Проверяет, что один ответ сохранен правильно"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn("English", self.my_survey.responses)

    def test_store_three_response(self):
        """"Проверяет, что три ответа были сохранены правильно."""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == "__main__":
    unittest.main()