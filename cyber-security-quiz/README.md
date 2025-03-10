# Cyber Security Quiz

This project is a simple command-line quiz application designed for cyber security revision. It allows users to test their knowledge by answering questions sourced from text files.

## Project Structure

```
cyber-security-quiz
├── src
│   ├── quiz_app.py        # Main application file that runs the quiz
│   ├── question_parser.py  # Contains functions to read and parse questions
│   └── utils.py           # Utility functions for scoring and formatting
├── data
│   ├── questions.txt      # Text file containing quiz questions
│   └── answers.txt        # Text file containing corresponding answers
├── tests
│   └── test_quiz.py      # Unit tests for the quiz application
├── requirements.txt       # Lists dependencies required for the project
└── README.md              # Documentation for the project
```

## Getting Started

To run the quiz application, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
4. Run the quiz application:
   ```
   python src/quiz_app.py
   ```

## How It Works

- The application loads questions from `data/questions.txt` and answers from `data/answers.txt`.
- Users are prompted to answer each question, and their responses are checked against the correct answers.
- At the end of the quiz, the user's score is displayed.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or additional features. 

## License

This project is open-source and available under the MIT License.