import unittest
from src.quiz.true_false import TrueFalse

class TestTrueFalse(unittest.TestCase):
    def setUp(self):
        self.question = "Is the sky blue?"
        self.answer = "yes"
        self.true_false_quiz = TrueFalse(self.question, self.answer)

    def test_question(self):
        self.assertEqual(str(self.true_false_quiz), self.question)

    def test_check_correct_answer(self):
        self.assertTrue(self.true_false_quiz.check("yes"))

    def test_check_incorrect_answer(self):
        self.assertFalse(self.true_false_quiz.check("no"))

    def test_ask_method(self):
        with unittest.mock.patch('builtins.input', return_value='yes'):
            self.assertTrue(self.true_false_quiz.ask())

        with unittest.mock.patch('builtins.input', return_value='no'):
            self.assertFalse(self.true_false_quiz.ask())

if __name__ == '__main__':
    unittest.main()