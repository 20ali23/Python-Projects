#Kullanıcıyı karşılama mesajı
print("Welcome to the tip calculator!")

#Kullanıcıdan gerekli bilgileri alma
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give?"))
people = int(input("How many people to split the bill?"))

#Ödenecek tutar için matematiksel hesaplama
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

#Ödenecek tutarı kullanıcıya bildirme mesajı
print(f"Each person should pay: {final_amount}$ ")