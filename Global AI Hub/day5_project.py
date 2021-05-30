# Final Project – Knowledge Competition
# The program should consist of 10 questions in total, each question having only one correct answer.
# Adjust the answers of the questions according to case sensitivity.
# Each question should be worth 10 points.
# If the user answers 5 or fewer questions, they will be considered unsuccessful.
# If the user answers more than 5 questions correctly, they will be considered successful.

# STILL A WORK IN PROGRESS!!!

def categories(category_choice, question_num):
    if (category_choice == 'Pop Culture'):
        pop_culture = {"Q1": "ANS1",
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
        tuple_pairs = pop_culture.items()
        qs_ans = tuple_pairs[question_num - 1]



    if (category_choice == 'Sports'):
        sports = {"Q1": "ANS1",
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
        question = sports(question_num - 1)

    if (category_choice == 'Literature'):
        literature = {"Q1": "ANS1",
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
        question = literature(question_num - 1)

    if (category_choice == 'Music'):
        music = {"Q1": "ANS1",
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
        question = music(question_num - 1)

    return qs_ans



def scoreboard(score):
    pass


print("----------WELCOME TO THE KNOWLEDGE COMPETITION!!!----------")
print("The Knowlegde Competition consists of 10 questions, each woth of 10 points and each has an only one correct answer.")
print("Please be vary of case sensetivity when enterring answers.")
print("In order to win, you will need to answer 50% or more of the total questions correctly.")
print("Now that you are ready to play...The game will begin!")
print("-----------------------------------------------------------")

question_count = 1
while (question_count <= 10):
    print("Which category would you like question{} to be from?" .format(question_count))
    print("Possible categories are Pop Culture, Sports, Literature, Music.")
    category_choice = input("Please enter the category of your choice: ")
    if (category_choice != "Pop Culture" and category_choice != "Sports" and category_choice != "Literature" and category_choice != "Music"):
        category_choice = input("Please enter a valid choice: ")
    import random as rnd
    question_num = rnd.randint(1, 11)
    categories(category_choice, question_num)

    #print("Q1 (%s): %s" % (category_choice, question))
    input("Enter your answer for the question: ")
    break







