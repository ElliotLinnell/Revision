class TrueFalse(Quiz):
    def __init__(self, question, answer):
        super().__init__(question, answer)

    def check(self, response):
        return response.lower() == self.answer.lower()

    def ask(self):
        print(self.question)
        response = input("Enter 'True' or 'False': ")
        return self.check(response)