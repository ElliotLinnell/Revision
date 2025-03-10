import unittest
from src.quiz.matching import Matching

class TestMatching(unittest.TestCase):
    def setUp(self):
        self.question = "Match the following terms with their definitions."
        self.answer = {"Python": "A programming language", "HTML": "Markup language for web pages"}
        self.choices = ["Python", "HTML", "CSS", "JavaScript"]
        self.matching_quiz = Matching(self.question, self.answer, self.choices)

    def test_str(self):
        self.assertIn("Match the following terms with their definitions.", str(self.matching_quiz))

    def test_check_correct_answer(self):
        response = {"Python": "A programming language", "HTML": "Markup language for web pages"}
        self.assertTrue(self.matching_quiz.check(response))

    def test_check_incorrect_answer(self):
        response = {"Python": "Not a programming language", "HTML": "Markup language for web pages"}
        self.assertFalse(self.matching_quiz.check(response))

    def test_ask(self):
        # This test would require mocking input, which is not shown here
        pass

if __name__ == '__main__':
    unittest.main()