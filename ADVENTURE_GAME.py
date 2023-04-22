name = input("Type your name: ")
print("Hello", name + ". Get ready for a new adventure.")

while True:
    answer = input("Our destination is the INFINITY CASTLE. "
                   "But we have to go through the dark forest. "
                   "Choose your path carefully. "
                   "Type Right to go right, Left to go left and q to quit: ").lower()
    if answer == "left":
        print("You can see a river.")
        answer = input('Type swim to swim across the river and back to go back: ').lower()
        if answer == "swim":
            print("You got eaten by an alligator. You LOST!!")
            break
        elif answer == "back":
            print("You got back.")
        else:
            print("Not a valid option. You LOST!!")


    elif answer == "q":
        print("Goodbye",name)
        quit()


    elif answer == "right":
        print("You can see a bridge.")
        answer = input("Type cross to cross the bridge and back to go back: ").lower()
        if answer == "cross":
            answer = input("You crossed the bridge. "
                           "Now you can see a tunnel."
                           "Type go to go through the tunnel and back to go back: ").lower()
            if answer == "go":
                answer = input("You can see a stranger. "
                               "Talk to the stranger and he will show you the way."
                               "Type talk to talk to the stranger and back to go back: ").lower()
                if answer == "talk":
                    print("You got in the castle and you WON!!.")
                    break
                else:
                    print("You LOST!!")
                    break

            elif answer == "back":
                print("You got back.")
            else:
                print("Not a valid option.")

        elif answer == "back":
            print("You got back.")
        else:
            print("Not a valid option. You LOST!!")

    else:
        print("Not a valid option. You LOST!!")
print("Goodbye")

