class ScoreTracker:
    def __init__(self):
        self.score = 0
        self.total_questions = 0

    def add_score(self, points):
        self.score += points

    def increment_question_count(self):
        self.total_questions += 1

    def display_score(self):
        print(f"Your score: {self.score}/{self.total_questions}")

    def reset(self):
        self.score = 0
        self.total_questions = 0