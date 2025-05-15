import random
import time  


def load_qs(filename=r"C:\Users\Bismillah\Desktop\coding\CODSOFT\Rule Based Chatbot\trivia_questions.txt"):
    questions = []
    try:
        with open(filename, "r", encoding="utf-8") as file:  # Specify UTF-8 encoding
            for line in file:
                line = line.strip()  # Remove leading/trailing whitespace
                if line:  # Skip empty lines
                    parts = line.split("|")
                    if len(parts) == 3:
                        question, options, correct_answer = parts
                        questions.append({
                           "question": question,
                            "options": options.split(", "),  # Split options into a list
                            "correct_answer": correct_answer.strip().upper(),  #handle spacing, case
                        })
                    else:
                        print(f"Skipping invalid line: {line}")  # Inform about skipped lines
        if not questions: #check if questions list is empty
            print(f"Error: No valid questions found in {filename}.  File may be empty or improperly formatted.")
            return []

    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return []  # Return an empty list if the file doesn't exist
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []  # Return empty list on other exceptions

    return questions

def display_qs(qs_data):
    print(qs_data["question"])
    for option in qs_data["options"]:
        print(option)

def get_user_answer():
    while True:
        answer = input("Your answer (A, B, C, or D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            return answer
        else:
            print("Invalid input. Please enter A, B, C, or D.")

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def display_feedback(is_correct):
    if is_correct:
        print("Correct!")
    else:
        print("Incorrect.")

def calculate_score(correct_answers, total_questions):
    if total_questions == 0:
        return 0.0  # Avoid division by zero
    return (correct_answers / total_questions) * 100

def display_score(score):
    print(f"Your final score is: {score:.2f}%")

def play_trivia_game():
    questions = load_qs()
    if not questions:
        print("No questions to play. Exiting.")
        return

    random.shuffle(questions)  # Shuffle the questions
    correct_answers = 0
    total_questions = 0

    print("Welcome to the Trivia Game!")
    time.sleep(1) # add some delays.

    for qs_data in questions:
        display_qs(qs_data)
        user_answer = get_user_answer()
        is_correct = check_answer(user_answer, qs_data["correct_answer"])
        display_feedback(is_correct)
        if is_correct:
            correct_answers += 1
        total_questions += 1
        time.sleep(1.5) #short delay

    score = calculate_score(correct_answers, total_questions)
    display_score(score)

    print("Thanks for playing!")

if __name__ == "__main__":
    play_trivia_game()