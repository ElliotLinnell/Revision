class MultipleChoice(Quiz):
    def __init__(self, question, answer, choices):
        super().__init__(question, answer)
        self.choices = choices

    def __str__(self):
        return self.question + "\n" + "\n".join(self.choices)

    def check(self, response):
        return response == self.answer

    def ask(self):
        print(self.question)
        for i, choice in enumerate(self.choices):
            print(f"{i + 1}. {choice}")
        response = int(input("Enter the number of your answer: "))
        return self.check(self.choices[response - 1])