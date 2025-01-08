#Kullanıcıyı karşılama mesajı
print("Welcome to Python Pizza Deliveries!")

#Kullanıcıdan pizza bilgilerini alma
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

#Fatura oluşturma
bill = 0

#Pizza boyutunu karşılaştırma
if size == "S":
  #Faturaya 15 ekleme
  bill += 15

elif size == "M":
  #Faturaya 20 ekleme
  bill += 20

else:
  #Faturaya 25 ekleme
  bill += 25

#Peyniri karşılaştırma
if add_pepperoni == "Y":
  if size == "S":
    #Faturaya 2 ekleme
    bill += 2

  else:
    #Faturaya 3 ekleme
    bill += 3

#Peyniri karşılaştırma
if extra_cheese == "Y":
  #Faturaya 1 ekleme
  bill += 1

#Toplam faturayı kullanıcıya bildirme
print(f"Your final bill is: ${bill}.")