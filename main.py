import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Calculate score
def calculate_score(list_of_cards):
    score = sum(list_of_cards)
    if score == 21 and len(list_of_cards) == 2:
        score = 0
    elif score > 21:
        for elementos in list_of_cards:
            if elementos == 11:
                list_of_cards[list_of_cards.index(11)]=1
        score = sum(list_of_cards)
    return score

#Compare function
def compare(user,computer):
    if user == computer:
        print(f"\nIt is a draw. You scored {user} and I scored {computer}\n")
    elif computer == 0:
        print("\nYou lose, computer has Blackjack\n")
    elif user == 0:
        print("\nYou WIN, you have Blackjack\n")
    elif user > 21:
        print(f"\nYou lose, you went over 21 with {user}.\n")
    elif computer > 21:
        print(f"\nYou WIN with a score of {user} while computer has {computer}\n")
    else:
        if user > computer:
            print(f"\nYou WIN with a score of {user} while computer has {computer}\n")
        else:
            print(f"\nYou lose with a score of {user} while computer has {computer}\n")



play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

restart_game = True
while restart_game:
    print(logo)
    #TODO 1: Handle 2 cards to each player and calculate the score
    user_hand = random.choices(cards,k=2)
    computer_hand=random.choices(cards,k=2)
    #TODO 2: If blackjack at first, game over
    game_on = True
    while game_on:
        user_score = calculate_score(user_hand)
        if user_score == 0:
            user_score = "Blackjack"
        print(f"\nYour cards: {user_hand}, current score: {user_score}")
        computer_score = calculate_score(computer_hand)
        print(f"Computer's first card: {computer_hand[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_on = False
        elif user_score == 21:
            game_on = False
        else:
            another_card = input("Do you want to draw another card? Type"
                                 "'y' for yes or 'n' for no: ")
            if another_card == "y":
                user_hand += random.choices(cards, k=1)
            else:
                game_on = False
    while computer_score < 17:
        computer_hand += random.choices(cards, k=1)
        computer_score = calculate_score(computer_hand)

    compare(user_score,computer_score)

    re_start = input("\nDo you want to play again? Type 'y' or 'n': ")
    if re_start == "n":
        restart_game = False
    else:
        print("\n"*100)
