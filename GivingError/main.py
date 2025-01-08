#Kullanıcıdan boy ve kilo girişi alma
height = float(input("Height: "))
weight = int(input("Weight: "))

#Boyun 3 den büyük olup olmadığını kontrol etme
if height > 3:
    #Kullanıcıya hata mesajı verme
    raise KeyError("Human Height should not be over 3 meters.")

#BMI değerini hesaplama
bmi = weight / height ** 2

#BMI değerini kullanıcıya bildirme
print(bmi)