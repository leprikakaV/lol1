import unittest
from survey import AnonymousSurvey
class TestAnonmyoussSurvey(unittest.TestCase):
    """ТЕсты для класса AnonymousSurvey"""

    def test_store_single_response(self):
        """Проверяет, что один ответ сохранен правильно"""
        question = "What language?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("English")
        self.assertIn("English", my_survey.responses)

if __name__ == "__main__":
    unittest.main()