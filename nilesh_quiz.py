def main():
  """Runs the main quiz game loop."""
  questions = [
      {"question": "What is the capital of France?", "options": ["London", "Paris", "Berlin"], "answer": 1},
      {"question": "What is the largest planet in our solar system?", "options": ["Jupiter", "Mars", "Earth"], "answer": 0},
      {"question": "What is the meaning of life?", "options": ["42", "There is none", "It's up to you"], "answer": 2}
  ]

  score = 0

  for question in questions:
    print(question["question"])
    for i, option in enumerate(question["options"]):
      print(f"{i+1}. {option}")

    user_input = input("Enter your answer (1, 2, or 3): ")
    try:
      user_answer = int(user_input) - 1
      if user_answer == question["answer"]:
        print("Correct!")
        score += 1
      else:
        print(f"Incorrect. The correct answer is {question['options'][question['answer']]}")
    except ValueError:
      print("Invalid input. Please enter a number (1, 2, or 3).")

  print(f"Final Score: {score} out of {len(questions)}")

if __name__ == "_main_":
  main()