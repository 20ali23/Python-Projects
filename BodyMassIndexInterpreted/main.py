#Kullanıcıdan boy ve kilo bilgisi alma
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#BMI değerini hesaplama
BMI = round(weight / height ** 2)

#BMI değerini karşılaştırma
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")

elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")

elif BMI < 30:
    print(f"Your BMI is {BMI}, you are overwight.")

elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")

else:
    print(f"Your BMI is {BMI}, you are clinically obese.")