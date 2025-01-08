#Kullanıcının yaşını öğrenme
age = int(input("What is your current age? "))

#Doksan yaşına kadar kalan yıl sayısı
new_years = 90 - age

#Matematiksel hesaplama
days = new_years * 365
weeks = new_years * 52
months = new_years * 12

#Kalan gün-hafta-ay sayısını kullanıcıya bildirme
print(f"You have {days} days, {weeks} weeks, and {months} months left.")