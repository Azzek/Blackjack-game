import random 
import os 
import arts

def print_cards(cards):
    text = ""
    for card in cards:
        text += f"[{card}]"
    return text

def compare(player_score, computer_score):
    if computer_score == player_score or player_score > 21 and computer_score > 21: return "Draw!"
    elif computer_score == 0: return "You lose! Computer win witch Blackjack🤕"
    elif player_score == 0: return "You win witch blackjack! 😯"
    elif player_score > 21: return "you lose! 😑"
    elif computer_score > 21: return "You win! 😎"
    elif player_score > computer_score: return "You win!"
    elif player_score < computer_score: return "You lose!"

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_cart = random.choice(cards)
    return random_cart

def calculate_score(cards):
    if 11 in cards and sum(cards) > 21:
        cards[11] = 1
    if sum(cards) == 21 and 11 in cards and len(cards) == 2:
        return 0
    else:
        return sum(cards)
def play():
    print(arts.logo)
    player = []
    computer = []

    for _ in range(2):
        player.append(deal_card())
        computer.append(deal_card())
    

    player_score = calculate_score(player)
    computer_score = calculate_score(computer)

    print(f"Computer cards: {computer[0]} [x]")
    print(f"Your cards: {print_cards(player)} Current score: {player_score}")

    if player_score == 0 or computer_score == 0 :
        print(compare(player_score = player_score, computer_score = computer_score))
        return
        
    while player_score < 21 and player_score != 0:

        should_take =  input('Wanna take another card? type "n" or "y": ') 
        print("\n")

        if should_take == "n" or should_take == "y":

            if should_take == "y":

                player.append(deal_card())
                player_score = calculate_score(player)
                print(f"Your cards: {print_cards(player)} Current score: {player_score}")
                
            else:
                break
        
    while computer_score <= 16:
        computer.append(deal_card())
        computer_score = calculate_score(computer)

    print(f"Your final hand: {print_cards(player)} Current score: {player_score}")
    print(f"Computer cards: {print_cards(computer)} Current score: {computer_score}")
    print(compare(player_score = player_score, computer_score = computer_score))

while input('Type "y" to start game: ').lower() == "y":
    os.system("cls")
    play()

