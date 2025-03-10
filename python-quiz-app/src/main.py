class QuizApp:
    def __init__(self):
        self.score = 0
        self.quizzes = []

    def load_quizzes(self):
        from utils.file_reader import read_quiz_data
        self.quizzes = read_quiz_data()

    def start_quiz(self):
        for quiz in self.quizzes:
            if quiz.ask():
                self.score += 1
                print("Correct!")
            else:
                print("Incorrect. The correct answer was:", quiz.get_answer())
        print(f"Your final score is: {self.score}/{len(self.quizzes)}")

if __name__ == "__main__":
    app = QuizApp()
    app.load_quizzes()
    app.start_quiz()