#Random kütüphanesini içe aktarma
import random

#Taş-Kağıt-Makas resimleri
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Resimler için liste oluşturma
game_images = [rock, paper, scissors]

#Oyuncu için seçim yapmasını isteme
user_choice = int(input("What do you chose? Type 0 for Rock 1 for paper 2 for Scissors. \n"))

#Seçtiği resimi yazdırma
print(game_images[user_choice])

#Rastgele bilgisayar seçimi yapma ve ekrana yazdırma
print("Computer choice: ")
computer_choice = random.randint(0, 2)
print(game_images[computer_choice])

#Oyuncu ve bilgisayar seçimini karşılaştırıp kazananı belirleme
if user_choice >= 3 or user_choice < 0:
    print("You typed an ivalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw.")