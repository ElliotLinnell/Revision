def calculate_score(correct_answers, total_questions):
    return (correct_answers / total_questions) * 100

def format_output(question, user_answer, correct_answer):
    result = "Correct!" if user_answer == correct_answer else "Incorrect!"
    return f"Question: {question}\nYour Answer: {user_answer}\nResult: {result}"