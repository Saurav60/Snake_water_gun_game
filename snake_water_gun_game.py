import random

class SnakeWaterGunGame:
    """A class to represent the Snake-Water-Gun game."""
    
    choices = {'s': 'Snake', 'w': 'Water', 'g': 'Gun'}
    winning_combinations = {'s': 'g', 'w': 's', 'g': 'w'}  # Key loses to Value
    
    def __init__(self):
        """Initialize scores for both player and computer."""
        self.user_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        """Randomly select the computer's choice."""
        return random.choice(list(self.choices.keys()))

    def determine_winner(self, user_choice, comp_choice):
        """Determine the winner of a round."""
        if user_choice == comp_choice:
            return "tie"
        return "win" if self.winning_combinations[user_choice] == comp_choice else "lose"

    def play_round(self):
        """Play a single round of the game."""
        user_choice = input("\nYour turn: Snake(s), Water(w), or Gun(g)? ").lower()
        while user_choice not in self.choices:
            print("❌ Invalid input! Please enter 's' for Snake, 'w' for Water, or 'g' for Gun.")
            user_choice = input("Try again: ").lower()

        comp_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, comp_choice)

        # Display round results
        print(f"\nComputer chose: {self.choices[comp_choice]}")
        print(f"You chose: {self.choices[user_choice]}")

        if result == "tie":
            print("🤝 The game is a tie!")
        elif result == "win":
            print("🎉 You win this round!")
            self.user_score += 1
        else:
            print("😢 You lose this round!")
            self.computer_score += 1

    def play_game(self):
        """Run the game in a loop until the player wants to quit."""
        print("🎮 Welcome to the Snake-Water-Gun Game!\n")
        while True:
            self.play_round()
            print(f"\nCurrent Score: You 🏆 {self.user_score} - {self.computer_score} 💻 Computer")
            replay = input("\nDo you want to play again? (y/n): ").lower()
            if replay != 'y':
                print("\nThanks for playing! 🎉")
                break

if __name__ == "__main__":
    game = SnakeWaterGunGame()
    game.play_game()
