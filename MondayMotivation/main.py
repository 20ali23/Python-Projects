#Gerekli kütüphanelerin içe aktarılması
import smtplib
import datetime
import random

#Kullanılacak email ve şifre
MY_EMAIL = "alialcan122@gmail.com"
MY_PASSWORD = "plxybzohjwuulvlv"

#Güncel zaman bilgisine ulaşma
now = datetime.datetime.now()
weekday = now.weekday()

#Haftanın gününü karşılaştırma
if weekday == 0:

    #Dosya işlemleri
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    #Motivasyon mesajını gönderme
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )