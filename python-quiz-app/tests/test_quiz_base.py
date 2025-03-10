import unittest
from src.quiz.quiz_base import Quiz

class TestQuiz(unittest.TestCase):
    def setUp(self):
        self.quiz = Quiz("What is the capital of France?", "Paris")

    def test_question(self):
        self.assertEqual(self.quiz.question, "What is the capital of France?")

    def test_answer(self):
        self.assertEqual(self.quiz.answer, "Paris")

    def test_check_correct_answer(self):
        self.assertTrue(self.quiz.check("Paris"))

    def test_check_incorrect_answer(self):
        self.assertFalse(self.quiz.check("London"))

    def test_ask(self):
        # Mocking input to test the ask method
        with unittest.mock.patch('builtins.input', return_value='Paris'):
            self.assertTrue(self.quiz.ask())

if __name__ == '__main__':
    unittest.main()