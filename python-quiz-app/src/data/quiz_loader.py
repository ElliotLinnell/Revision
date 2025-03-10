def load_quiz_data(file_path):
    quizzes = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            question = lines[i].strip()
            answer = lines[i + 1].strip() if i + 1 < len(lines) else ''
            quizzes.append((question, answer))
    return quizzes

def load_all_quizzes(directory):
    import os
    all_quizzes = {}
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            all_quizzes[filename] = load_quiz_data(file_path)
    return all_quizzes