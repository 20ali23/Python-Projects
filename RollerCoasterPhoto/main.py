#Kullanıcıyı karşılama mesajı
print("Welcome to the rollercoaster!")

#Kullanıcının yaşını öğrenme
height = int(input("What is your height in cm?"))

#Fatura oluşturma
bill = 0

#Kullanıcının boyunu karşılaştırma
if height > 120:

  #Kullanıcının yaşını öğrenme
  age = int(input("What is your age?"))

  #Kullanıcının yaşını karşılaştırma
  if age < 12:
    #Fatura değeri 5
    bill = 5

  elif age < 18:
    #Fatura değeri 7
    bill = 7

  else:
    #Fatura değeri 12
    bill = 12

  #Kullanıcıdan fotoğraf isteyip istemediğini öğrenme
  photo = input("Do you want a photo taken? Y or N.")

  #Fotoğraf isteyip istemediğini karşılaştırma
  if photo == 'Y':
    #Fatura değerine 3 ekleme
    bill += 3
    #Toplam faturayı kullanıcıya bildirme
    print(f"Your final is {bill}.")

  else:
    print(f"Your final is {bill}.")

else:
  print("Sorry, you have to grow taller before you can ride.")