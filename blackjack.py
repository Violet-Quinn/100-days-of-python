import random


#returns a random card from the deck
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

#take list of cards and calculate score
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
         cards.remove(11)
         cards.append(1)
    return sum(cards)

def compare_score(p_score, c_score):
    if p_score==c_score:
        return "Draw"
    elif c_score==0:
        return "You lose, opponent has Blackjack"
    elif p_score==0:
        return "You win with a Blackjack"
    elif p_score>21:
        return "You lose, you went over 21"
    elif c_score>21:
        return "Opponent went over, You win"
    elif p_score>c_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    player_cards=[]
    computer_cards=[]
    player_score=-1
    computer_score=-1
    is_game_over=False

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        player_score=calculate_score(player_cards)
        computer_score=calculate_score(computer_cards)
        print(f"player cards {player_cards} , current score: {player_score}")
        print(f"computer card {computer_cards[0]}")

        if player_score==0 or computer_score==0 or player_score>21:
            is_game_over=True
        else:
            ask_player_draw=input(f'Type "y" to get another card, type "n" to pass')
            if ask_player_draw=="y":
                player_cards.append(deal_card())
            else:
                is_game_over=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"\nFinal player cards: {player_cards}, final score: {player_score}")
    print(f"Final computer cards: {computer_cards}, final score: {computer_score}")

    result=compare_score(player_score,computer_score)
    print(result)

while input("Do you want to play a game of Blackjack? Type y or n")=="y":
    print("\n"*20)
    play_game()