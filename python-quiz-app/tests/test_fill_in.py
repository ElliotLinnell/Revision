import unittest
from src.quiz.fill_in import FillIn

class TestFillIn(unittest.TestCase):
    def setUp(self):
        self.question = "What is the capital of France?"
        self.answer = "Paris"
        self.fill_in_quiz = FillIn(self.question, self.answer)

    def test_check_correct_answer(self):
        self.assertTrue(self.fill_in_quiz.check("Paris"))

    def test_check_incorrect_answer(self):
        self.assertFalse(self.fill_in_quiz.check("London"))

    def test_ask_question(self):
        with unittest.mock.patch('builtins.input', return_value='Paris'):
            self.assertTrue(self.fill_in_quiz.ask())

    def test_get_question(self):
        self.assertEqual(self.fill_in_quiz.get_question(), self.question)

    def test_get_answer(self):
        self.assertEqual(self.fill_in_quiz.get_answer(), self.answer)

if __name__ == '__main__':
    unittest.main()