#Kullanıcıdan boy ve kilo bilgisi alma
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#BMI değerini hesaplama
BMI = int(weight) / float(height) ** 2
new_BMI = int(BMI)

#BMI değerini kullanıcıya bildirme
print(new_BMI)