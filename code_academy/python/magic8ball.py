name = input("Please enter your name: ")
question = input("Please enter your question %s: " %name)

answers = ["Yes - definitely.", "It is decidedly so.", "Without a doubt.",
           "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
           "My sources say no.", "Outlook not so good.", "Very doubtful."]

import random as rn
rand_num = rn.randint(1,9)
ans = answers[rand_num]

print("\n")
print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + ans)