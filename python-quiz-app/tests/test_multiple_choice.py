import unittest
from src.quiz.multiple_choice import MultipleChoice

class TestMultipleChoice(unittest.TestCase):

    def setUp(self):
        self.question = "What is the capital of France?"
        self.answer = "Paris"
        self.choices = ["Berlin", "Madrid", "Paris", "Rome"]
        self.quiz = MultipleChoice(self.question, self.answer, self.choices)

    def test_question(self):
        self.assertEqual(str(self.quiz), self.question + "\n" + "\n".join(self.choices))

    def test_check_correct_answer(self):
        self.assertTrue(self.quiz.check("Paris"))

    def test_check_incorrect_answer(self):
        self.assertFalse(self.quiz.check("Berlin"))

    def test_ask(self):
        with unittest.mock.patch('builtins.input', return_value='3'):
            self.assertTrue(self.quiz.ask())

if __name__ == '__main__':
    unittest.main()