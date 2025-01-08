#Numara listei oluşturma
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

#Liste içindeki numaraların ikiye bölünüp bölünmediğini kontrol edip yeni listeye ekleme
result = [number for number in numbers if number % 2 == 0]

#Listeyi kullanıcıya bildirme
print(result)