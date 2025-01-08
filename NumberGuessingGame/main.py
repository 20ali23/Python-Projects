import random

#Rastgele sayı üretme
number = random.randint(1, 101)

#Kullanıcıyı karşılama mesajı
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

#Kullanıcıdan seviye zorluğu seçmesini isteme
choose = input("Choose a difficulty. Type 'easy' or 'hard': ")

#Zor seviye
if choose == 'hard':
  
  #Kullanıcının beş canının olduğunu söyleme
  print("You have 5 attempts remaining to guess the number.")
  int_game1 = 5
  
  #Oyunu can sayısına göre döngüye sokma
  while int_game1 > 0:
    
    #Sayı tahmini alma
    guess1 = int(input("Make a guess: "))
    
    #Tahmin rastgele üretilen sayıya eşit mi?
    if guess1 == number:
      print(f"You got it! The answer was {number} ")
      int_game1 = 0

    #Rastgele üretilen sayı tahminden küçük mü?
    elif guess1 > number:
      print("Too high.")
      print("Guess again.")
      int_game1 -= 1
      print(f"You have {int_game1} attempts remaining to guess the number.")
      
      #Can sayısını kontrol etme
      if int_game1 == 0:
        print("You've run out of guesses, you lose.")

    #Rastgele üretilen sayı tahminden büyük mü?
    elif guess1 < number :
      print("Too low.")
      print("Guess again.")
      int_game1 -= 1
      print(f"You have {int_game1} attempts remaining to guess the number.")

      #Can sayısını kontrol etme
      if int_game1 == 0:
        print("You've run out of guesses, you lose.")

#Kolay seviye
elif choose == 'easy':

  #Kullanıcının on canının olduğunu söyleme
  print("You have 10 attempts remaining to guess the number.")
  int_game2 = 10
  
  #Can sayısına göre oyunu döngüye sokma
  while int_game2 > 0:

    #Sayı tahmini alma
    guess2 = int(input("Make a guess: "))
    
    #Tahmin rastgele üretilen sayıya eşit mi?
    if guess2 == number:
      print(f"You got it! The answer was {number} ")
      int_game2 = 0
      
    #Rastgele üretilen sayı tahminden küçük mü?
    elif guess2 > number:
      print("Too high.")
      print("Guess again.")
      int_game2 -= 1
      print(f"You have {int_game2} attempts remaining to guess the number.")
      
      #Can sayısını kontrol etme
      if int_game2 == 0:
        print("You've run out of guesses, you lose.")

    #Rastgele üretilen sayı tahminden büyük mü?
    elif guess2 < number :
      print("Too low.")
      print("Guess again.")
      int_game2 -= 1
      print(f"You have {int_game2} attempts remaining to guess the number.")
      
      #Can sayısını kontrol etme
      if int_game2 == 0:
        print("You've run out of guesses, you lose.")