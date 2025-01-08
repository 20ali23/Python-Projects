#Kullanıcıyı karşılama mesajı
print("Welcome to the rollercoaster!")

#Kullanıcının boyunu öğrenme
height = int(input("What is your height in cm?"))

#Kullanıcının boyunu karşılaştırma
if height > 120:

  #Kullanıcının yaşını öğrenme
  age = int(input("What is your age?"))

  #Kullanıcının yaşını karşılaştırma
  if age <= 18:
    print("Please pay 7$.")

  else:
    print("Please pay 12$.")

else:
  print("Sorry, you have to grow taller before you can ride.")