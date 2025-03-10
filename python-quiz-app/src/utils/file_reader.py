def read_quiz_file(file_path):
    quizzes = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            question = lines[i].strip()
            answer = lines[i + 1].strip() if i + 1 < len(lines) else ''
            quizzes.append((question, answer))
    return quizzes

def read_quiz_files(file_paths):
    all_quizzes = []
    for file_path in file_paths:
        all_quizzes.extend(read_quiz_file(file_path))
    return all_quizzes