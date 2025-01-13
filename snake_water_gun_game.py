#we need to import random module to generate random choices by computer.
import random

def game_win(comp, you):
    # If two values are equal declare a tie
    if comp == you:
        return None
    # Check all possibilities when the computer chooses Snake (s)
    elif comp == 's':
        return you == 'g'  # Gun beats Snake
    # Check all possibilities when the computer chooses Water (w)
    elif comp == 'w':
        return you == 's'  # Snake beats Water
    # Check all possibilities when the computer chooses Gun (g)
    elif comp == 'g':
        return you == 'w'  # Water beats Gun

# Computer's turn
print("Computer's turn: Snake(s), Water(w), or Gun(g)?")
randNO = random.randint(1, 3)
comp = 's' if randNO == 1 else 'w' if randNO == 2 else 'g'

# User's turn
you = input("Your turn: Snake(s), Water(w), or Gun(g)? ").lower()

# Check for invalid input
if you not in ['s', 'w', 'g']:
    print("Invalid input! Please enter 's' for Snake, 'w' for Water, or 'g' for Gun.")
else:
    a = game_win(comp, you)

    print(f"Computer chose: {comp}")
    print(f"You chose: {you}")

    if a is None:
        print("The game is a tie!")
    elif a:
        print("You win!!!!")
    else:
        print("You lose!!!!")


