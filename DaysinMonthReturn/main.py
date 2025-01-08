#Artık yıl olup olmadığını kontrol etme
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

#Fonksiyon oluşturma
def days_in_month(year, month):
    #Hatalı giriş kontrolü
    if month > 12 and month < 1:
        return "İnvalid month"

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]

#Kullanıcıdan yıl ve ay girişi alma
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

#Fonksiyonu çağırma
print(days_in_month(year, month))