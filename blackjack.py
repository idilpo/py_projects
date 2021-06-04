# GAME OF BLACKJACK

# STILL A WORK IN PROGRESS!!!

def cards():
    pass

def main():
    print("--------------WELCOME TO BLACKJACK!!!--------------")
    choice = input("Would you like to see the rules of the game?\nEnter Y for yes, N for no: ")
    if (choice == 'Y'):
        print("rules rules rules")
        print("Now that you are ready to play...The game will begin!")
        print("-----------------------------------------------------------")
    elif (choice == 'N'):
        pass
    else:
        while (choice != 'Y' and choice == 'N'):
            choice = input("Please enter a valid input: ")







if __name__ == '__main__':
  main()