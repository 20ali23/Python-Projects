#Kullanıcıdan iki basamaklı sayı girişi alma
two_digit_number = input("Type a two digit number: ")

#Girilen sayıyı basamaklarına ayırma
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

#Basamak rakamlarını toplama
result = int(first_digit + second_digit)

#Sonucu kullanıcıya bildirme
print(result)