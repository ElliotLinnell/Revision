import unittest
from src.question_parser import load_questions
from src.quiz_app import Quiz

class TestQuiz(unittest.TestCase):

    def setUp(self):
        self.questions = load_questions()
        self.quiz = Quiz(self.questions)

    def test_load_questions(self):
        self.assertGreater(len(self.questions), 0, "Questions should be loaded from the file.")

    def test_quiz_initialization(self):
        self.assertEqual(len(self.quiz.questions), len(self.questions), "Quiz should have the same number of questions as loaded.")

    def test_check_answer_correct(self):
        question = self.questions[0]
        correct_answer = self.quiz.answers[0]
        self.assertTrue(self.quiz.check_answer(question, correct_answer), "Should return True for correct answer.")

    def test_check_answer_incorrect(self):
        question = self.questions[0]
        incorrect_answer = "wrong_answer"
        self.assertFalse(self.quiz.check_answer(question, incorrect_answer), "Should return False for incorrect answer.")

if __name__ == '__main__':
    unittest.main()