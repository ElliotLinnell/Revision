def load_quiz_data(questions_path, answers_path):
    """Load questions and answers from text files."""
    with open(questions_path, 'r') as q_file:
        questions = [q.strip() for q in q_file.readlines() if q.strip()]
    
    with open(answers_path, 'r') as a_file:
        answers = [a.strip() for a in a_file.readlines() if a.strip()]
    
    # Ensure we have matching questions and answers
    if len(questions) != len(answers):
        print("Warning: Number of questions and answers don't match!")
        # Use the smaller length to avoid index errors
        min_length = min(len(questions), len(answers))
        questions = questions[:min_length]
        answers = answers[:min_length]
    
    return questions, answers

def run_quiz():
    """Run the cyber security quiz."""
    print("\n----- CYBER SECURITY QUIZ -----\n")
    
    try:
        questions, answers = load_quiz_data('questions.txt', 'answers.txt')
    except FileNotFoundError:
        print("Error: Question or answer file not found.")
        return
    
    if not questions:
        print("No questions found. Please add questions to the text file.")
        return
    
    score = 0
    total = len(questions)
    
    for i, question in enumerate(questions):
        print(f"Question {i+1}/{total}:")
        print(f"{question}")
        user_answer = input("\nYour answer: ")
        
        if user_answer.lower() == answers[i].lower():
            print("✓ Correct!\n")
            score += 1
        else:
            print(f"✗ Incorrect. The correct answer is: {answers[i]}\n")
    
    percentage = (score / total) * 100
    print(f"\n----- Quiz Complete -----")
    print(f"You scored: {score}/{total} ({percentage:.1f}%)")
    
    if percentage >= 90:
        print("Excellent!")
    elif percentage >= 70:
        print("Good job!")
    elif percentage >= 50:
        print("Keep studying!")
    else:
        print("More revision needed.")

if __name__ == "__main__":
    run_quiz()