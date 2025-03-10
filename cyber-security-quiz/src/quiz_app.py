def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions = file.readlines()
    return [question.strip() for question in questions]

def load_answers(file_path):
    with open(file_path, 'r') as file:
        answers = file.readlines()
    return [answer.strip() for answer in answers]

def run_quiz():
    questions = load_questions('../data/questions.txt')
    answers = load_answers('../data/answers.txt')
    
    score = 0
    for i, question in enumerate(questions):
        print(f"Q{i + 1}: {question}")
        user_answer = input("Your answer: ")
        if user_answer.lower() == answers[i].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answers[i]}")
    
    print(f"You scored {score} out of {len(questions)}.")

if __name__ == "__main__":
    run_quiz()