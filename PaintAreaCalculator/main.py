#Matematik kütüphanesini içe aktarma
import math

#Hesaplama fonksiyonu oluşturma
def paint_calc(height, width, cover):
    kutu = math.ceil((test_h * test_w) / coverage)
    print(f"You'll need {kutu} cans of paint.")

#Kullanıcıdan en ve boy girişi alma
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))

coverage = 5

#Fonskiyonu çağırıp girdilerini verme
paint_calc(height=test_h, width=test_w, cover=coverage)