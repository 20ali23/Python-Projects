import random

#Rastgele kart çekme fonksiyonu
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

#BlackJack ve Ace belirleme
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Puan karşılaşılaştırma fonksiyonu
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw."
    elif computer_score == 0:
        return "Lose opponent has Blackack."
    elif user_score == 0:
        return "Win with a BlackJack."
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    #Oyuncu ve bilgisayar için kart seçildi
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        #Oyuncunun ve Bilgisayarın kartlarını toplama 
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"You'r cards: {user_cards}, current score {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}")

        #Skorlarda sıfır ve yirmi birden büyük değer olup olmadığını kontrol etme
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            #Kart çekmek isteyip istemediğini belirleme 
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    #Bilgisayar için kart seçimi
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"You final hand: {user_cards}, final score: {user_score}.")
    print(f"You final hand: {computer_cards}, final score: {computer_score}.")
    print(compare(user_score, computer_score))

#Oyuna devam edip etmemeyi belirleme
while input("Do you want to play a game of BlacJack? Type 'y' or 'n': ") == "y":
    play_game()