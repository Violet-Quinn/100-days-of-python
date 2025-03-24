print('''

                                                    ____
                                         v        _(    )
        _ ^ _                          v         (___(__)
       '_\V/ `
       ' oX`
          X                            v
          X             
          X                                                 .
          X        \O/                                      |\
          X.a##a.   M                                       |_\
       .aa########a.>>                                    __|__
    .a################aa.                                 \   /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')

print("Welcome to Treasure Island")
print("Find the Treasure")
choice1=input('You\'re at a crossroad, where do you want to go? Type "Left" or "Right".').lower()
if choice1=="left":
    print("You fell into a hole, Game Over!")
elif choice1=="right":
    choice2=input('You have come to a lake, there is an island in the middle of the lake. '
                  'Type "wait" to wait for a boat or "swim" to swim to the island.').lower()
    if choice2=="swim":
        print("You were attacked by Trouts, Game Over!")
    elif choice2=="wait":
        choice3=input('You\'ve reached the island, there are three doors in front of you, '
                      'Red, Blue and Green. Type "Red", "Blue" or "Yellow" to choose a door.').lower()
        if choice3=="red":
            print("Burned by Fire, Game Over")
        elif choice3=="blue":
            print("Eaten by Beasts, Game Over")
        elif choice3=="yellow":
            print("You Win!!")
        else:
            print("Wrong input")
    else:
        print("Wrong input")

else:
    print("Wrong input")
