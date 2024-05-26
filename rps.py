import random

print("Let's play Rock Paper Scissors!!!")

picks = ["Rock", "Paper", "Scissors"]

even_expressions = [
    "Ahhh!! That's cute.",
    "OMG what are you? A Wizard.",
    "See, I can read your mind.",
    "You smell good today. *wink*"
]

win_expressions = [
    "Oww yeah. You think you're better than me?!",
    "K. I give you that.",
    "Go celebrate your victory!",
    "Go again."
]

lose_expressions = [
    "Suck on that, Loser!",
    "You think you got it, but you don't.",
    "Looks like someone ran out of luck again.",
    "Don't worry, losing isn't that bad."
]

def the_input():
    user_name = input("Enter your name: ")
    while True:
        pick = input("Enter (Rock, Paper, Scissors) or 'q' to quit: ").lower()
        if pick in ["rock", "paper", "scissors", 'q']:
            return user_name, pick
        else:
            print("Invalid input. Please enter Rock, Paper, or Scissors.")

def pick_one():
    random_pick = random.choice(picks).lower()
    print("Computer picked:", random_pick.capitalize())
    return random_pick

def logic(pick, random_pick, scores):
    if random_pick == pick:
        print(random.choice(even_expressions))
    elif (random_pick == "rock" and pick == "scissors") or \
         (random_pick == "paper" and pick == "rock") or \
         (random_pick == "scissors" and pick == "paper"):
        print(random.choice(lose_expressions))
        scores["computer_wins"] += 1
    else:
        print(random.choice(win_expressions))
        scores["user_wins"] += 1

def click_q(user_name, scores):
    print(f"\n{user_name} wins {scores['user_wins']} times.")
    print(f"Computer wins {scores['computer_wins']} times.\n")
    if scores["user_wins"] > scores["computer_wins"]:
        print(f"Final winner is ---{user_name}---\n")
    elif scores["user_wins"] < scores["computer_wins"]:
        print("Try again, Buddy. You lose.\n")
    else:
        play_again = input("Match is a draw. Wanna play again? (Y/N): ").lower()
        if play_again == 'y':
            main()
        else:
            print("Thanks for playing!")
            quit()

def main():
    scores = {"user_wins": 0, "computer_wins": 0}
    user_name, pick = the_input()
    while pick != 'q':
        computer_pick = pick_one()
        logic(pick, computer_pick, scores)
        user_name, pick = the_input()
    click_q(user_name, scores)

if __name__ == "__main__":
    main()
