class Quiz():
    def __init__(self, question, answer, file=None):
        self.question = question
        self.answer = answer
        self.file = file

    def __str__(self):
        return self.question

    def check(self, response):
        return response == self.answer

    def ask(self):
        print(self.question)
        response = input("Enter your answer: ")
        return self.check(response)

    def get_answer(self):
        if self.file:
            answer = self.file.readline().strip()
            return answer
        return self.answer

    def get_question(self):
        if self.file:
            question = self.file.readline().strip()
            return question
        return self.question

    def create_quiz(self):
        if self.file:
            question = self.file.readline().strip()
            answer = self.file.readline().strip()
            return question, answer
        return self.question, self.answer

    def get_quiz(self):
        return self.question, self.answer