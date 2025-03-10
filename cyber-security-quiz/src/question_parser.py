def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions = file.readlines()
    return [question.strip() for question in questions]

def load_answers(file_path):
    with open(file_path, 'r') as file:
        answers = file.readlines()
    return [answer.strip() for answer in answers]