#Random kütüphanesini içe aktarma
import random

#Kullanıcıdan isim girişi alma
names_string = input("Give me everybody's names, separated by a comma\. (Tom|Dick|Harry) ")

#İsim girişlerini listeye çevirme
names = names_string.split(", ")

#Rastgele kişi seçme
random_string = random.randint(0, len(names) - 1)
person_who_will_pay = names[random_string]

#Seçilen rastgele kişiyi kullanıcıya bildirme
print(person_who_will_pay + " is going to buy the meal today!$")