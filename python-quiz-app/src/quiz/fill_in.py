class FillIn(Quiz):
    def __init__(self, question, answer):
        super().__init__(question, answer)

    def check(self, response):
        return response.strip().lower() == self.answer.strip().lower()

    def ask(self):
        print(self.question)
        response = input("Enter your answer: ")
        return self.check(response)