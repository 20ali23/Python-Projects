#Kullanıcıyı karşılama mesajı
print("Welcome to the Love Calculator!")

#Kullanıcıdan iki isim girişi alma
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

#İsimleri birleştirme
name12 = name1 + name2

#Birleştirilen isim içindeki true harflerini sayma
t = name12.count("t")
r = name12.count("r")
u = name12.count("u")
e = name12.count("e")

#Birleştirilen isim içindeki love harflerini sayma
l = name12.count("l")
o = name12.count("o")
v = name12.count("v")
e = name12.count("e")

#Harfleri toplama
true = t + r + u + e
love = l + o + v + e

#Toplamı string olarak birleştirme
score = int(str(true) + str(love))

#Sonucu karşılaştırıp kullanıcıya mesaj verme
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")

elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}.")