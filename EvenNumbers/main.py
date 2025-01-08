#Toplam değişkeni oluşturma
total1 = 0

#0-100 aralığında ikişer ikişer sayıp toplama
for number in range(0, 101, 2):
  total1 += number
print(total1)

#Toplam değişkeni oluşturma
total2 = 0

#0-100 aralığında sayının ikiye bölünüp bölünmediğini kontrol edip toplama
for number in range(1, 101):
  if number % 2 == 0:
    total2 += number
print(total2)