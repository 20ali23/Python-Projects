#Kullanıcıyı karşılama mesajı
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Kullanıcıdan yön girişi alma
choice1 = input('You are at a crossroad, where do you want to go? Type "left" or "right".').lower()

#Yön karşılaştırma
if choice1 == "left":
    
    #Kullanıcıdan durum girişi alma
    choice2 = input('You\'ve come to a lake. There is an island in in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    
    #Durum karşılaştırma
    if choice2 == "wait":
        
        #Kullanıcıdan renk girişi alma
        choice3 = input("You arrive at the island unharned. There is a house with 3 doors. One red, one yellow, and one blue Which colour do you choose?").lower()
        
        #Renk karşılaştırma
        if choice3 == "red":
            print("It\'s a room full of fire.Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")