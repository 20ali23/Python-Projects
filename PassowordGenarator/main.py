#Random kütüphanesini içe aktarma
import random

#Harf-Rakam-Sembol listesi oluşturma
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Kullanıcıyı karşılama mesajı
print("Welcome to the PyPassword Generator!")

#Kullanıcıdan şifre için kullanılcak harf,rakam ve sembol adedini öğrenme
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Boş liste oluşturma
password_list = []

#Rastgele harf seçip boş listeye ekleme
for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

#Rastgele sembol seçip boş listeye ekleme
for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

#Rastgele rakam seçip boş listeye ekleme
for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

#Oluşturulan listeyi karıştırma
random.shuffle(password_list)

#Karıştırılan listeyi for döngüsü ile değişkene kaydetme
password = ""
for char in password_list:
  password += char
  
#Oluşturulan şifreyi kullanıcıya bildirme
print(f"Your password is: {password}")