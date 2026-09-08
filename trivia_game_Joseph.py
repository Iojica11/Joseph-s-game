# hello, this is my trivia game, this is my first real hands-on project
# I use random for different question everytime the program is running
import random as rand
from time import sleep
import time as t
# store answwers in a dictionary to have keys asociated with values 
list_q = {"Which keyword is used to define a function in Python?": "def",
          "Which built-in function outputs text to the console?": "print()",
          "What is the function's name that deletes objects?": "del",
          "Which function returns the length of a list or string?": "len()",
          "Which symbol is used for single-line comments in Python?": "Hash (#)"
}

# now we pick the questions
# we define a function that will do the hard part
def py_trivia_Joseph():
    questions_list = list(list_q.keys())
    total_questions = 5
    score = 0

    # we select how many question to be displayed
    selected_question = rand.sample(questions_list, total_questions)
    print(selected_question)

    for idx, question in enumerate(selected_question):
        print(f"{idx + 1}. {question}")
        user_answer = input("Your answer is: ").lower().strip() #lower for rapid ans and strip for typing error by the user
        correct_ans = list_q[question]

        if user_answer == correct_ans.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong..The correct answer is: {correct_ans}.\n")
    
    for i in range(1, 4):
        print("Loading" + '.' * i, end='\r')
        t.sleep(0.5)
    print(f"Game over! your final score: {score}/{total_questions}")

py_trivia_Joseph()


