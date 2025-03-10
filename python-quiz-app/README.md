# Python Quiz Application

This project is a Python-based quiz application designed for revision purposes. It allows users to answer questions from various categories, including general knowledge, science, and history. The questions and answers are read from text files, making it easy to update and expand the quiz content.

## Project Structure

```
python-quiz-app
├── src
│   ├── main.py                # Entry point of the application
│   ├── quiz                   # Contains quiz-related classes
│   │   ├── __init__.py
│   │   ├── quiz_base.py       # Base class for quizzes
│   │   ├── true_false.py      # True/False question implementation
│   │   ├── multiple_choice.py  # Multiple choice question implementation
│   │   ├── fill_in.py         # Fill-in-the-blank question implementation
│   │   └── matching.py        # Matching question implementation
│   ├── utils                  # Utility functions
│   │   ├── __init__.py
│   │   ├── file_reader.py     # Functions for reading quiz data from files
│   │   └── score_tracker.py    # Functions for tracking user scores
│   └── data                   # Data loading functions
│       ├── __init__.py
│       └── quiz_loader.py     # Functions for loading quiz data
├── tests                      # Unit tests for the application
│   ├── __init__.py
│   ├── test_quiz_base.py      # Tests for the Quiz class
│   ├── test_true_false.py     # Tests for the TrueFalse class
│   ├── test_multiple_choice.py # Tests for the MultipleChoice class
│   ├── test_fill_in.py        # Tests for the FillIn class
│   └── test_matching.py       # Tests for the Matching class
├── quiz_data                  # Contains quiz question files
│   ├── general_knowledge.txt   # General knowledge questions
│   ├── science.txt            # Science questions
│   └── history.txt            # History questions
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Getting Started

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd python-quiz-app
   ```

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```
   python src/main.py
   ```

## How to Add Questions

To add new questions, simply create or edit the text files in the `quiz_data` directory. Each question should be followed by its answer on the next line.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.