#Numara listesi
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

#Numbers dizesindeki sayıları for döngüsü ile tek tek üzerinde geçerek karesini alıp yeni listeye ekler
squared_numbers = [pow(number, 2) for number in numbers]

#Yeni listeyi yazdırma
print(squared_numbers)