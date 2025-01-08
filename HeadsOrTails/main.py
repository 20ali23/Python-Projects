#Random kütüphanesini içe aktarma
import random

#0 ile 1 arasında rastgele tam sayı seçer 
random_number = random.randint(0, 1)

#Rastgele sayıyı karşılaştırma
if random_number == 1:
    print("Heads")

else:
    print("Tails")