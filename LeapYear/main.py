#Kullanıcıdan yıl girişi alma
year = int(input("Which year do you want to check? "))

#Girilen yılın artık yıl olup olmadığını kotrol etme
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")