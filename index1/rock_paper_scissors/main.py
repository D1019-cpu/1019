import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors:\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "It's a tie."
    
    # r > s, s > p, p > r
    if is_win(user,computer):
        return f"You won! Computer is {computer}"
    
    return f"You lost! Computer is {computer}"

def is_win(player, computer):
    # return true if player wins
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') \
        or (player == 'p' and computer == 'r'):
        return True


if __name__ == '__main__':
    print(play())
