# Final Project – Knowledge Competition
# The program should consist of 10 questions in total, each question having only one correct answer.
# Adjust the answers of the questions according to case sensitivity.
# Each question should be worth 10 points.
# If the user answers 5 or fewer questions, they will be considered unsuccessful.
# If the user answers more than 5 questions correctly, they will be considered successful.

# still a work in progress!!!

import random as rnd
print("------WELCOME TO THE KNOWLEDGE COMPETITION!!!------")
print("Would you like to see the rules of the competition?")
choice = input("Enter Y for yes, N for no: ")

def instructions():
    print("The Knowlegde Competition consists of 10 questions, each woth of 10 points and each has an only one correct answer.")
    print("Please be vary of case sensetivity when enterring answers.")
    print("In order to win, you will need to answer 50% or more of the total questions correctly.")
    print("Now that you are ready to play...The game will begin!")


def game():
    question_count = 10
    while(question_count != 0):
        print("Which category would you like your first question to be from?")
        print("Possible categories are Pop Culture, Sports, Literature, Music.")
        def categories():
            category_choice = input("Please enter the category of your choice: ")
            if (category_choice == 'Pop Culture'):
                qs_ans = {"Q1" : "ANS1",
                          "Q2": "ANS2",
                          "Q3": "ANS3",
                          "Q4": "ANS4",
                          "Q5": "ANS5",
                          "Q6": "ANS6",
                          "Q7": "ANS7",
                          "Q8": "ANS8",
                          "Q9": "ANS9",
                          "Q10": "ANS10",
                }

            elif (category_choice == 'Sports'):
                qs_ans = {"Q1": "ANS1",
                          "Q2": "ANS2",
                          "Q3": "ANS3",
                          "Q4": "ANS4",
                          "Q5": "ANS5",
                          "Q6": "ANS6",
                          "Q7": "ANS7",
                          "Q8": "ANS8",
                          "Q9": "ANS9",
                          "Q10": "ANS10",
                          }

            elif (category_choice == 'Literature'):
                qs_ans = {"Q1": "ANS1",
                          "Q2": "ANS2",
                          "Q3": "ANS3",
                          "Q4": "ANS4",
                          "Q5": "ANS5",
                          "Q6": "ANS6",
                          "Q7": "ANS7",
                          "Q8": "ANS8",
                          "Q9": "ANS9",
                          "Q10": "ANS10",
                          }
            elif (category_choice == 'Music'):
                qs_ans = {"Q1": "ANS1",
                          "Q2": "ANS2",
                          "Q3": "ANS3",
                          "Q4": "ANS4",
                          "Q5": "ANS5",
                          "Q6": "ANS6",
                          "Q7": "ANS7",
                          "Q8": "ANS8",
                          "Q9": "ANS9",
                          "Q10": "ANS10",
                          }
            else:
                while (category_choice != 'Pop Culture' or category_choice != 'Sports' or category_choice != 'Literature' or category_choice != 'Music'):
                    category_choice = input("Please enter a valid choice: ")
    categories()
    def scoreboard(score):
        pass




if (choice == 'Y'):
    instructions()
    game()
elif (choice == 'N'):
    game()
else:
    while (choice != 'Y' or choice != 'N'):
        choice = input("Please enter a valid input: ")



