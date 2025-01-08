#Kullanılacak kütüphanenin içe aktarılması
import smtplib
import datetime

#Kullanılacak email ve şifre bilgisi
MY_EMAIL = "alialcan122@gmail.com"
MY_PASSWORD = "kpltgommzurxtbku"

#Kişinin doğum ayı ve doğum günü bilgisi
MY_MONTH = 12
MY_DAY = 20

#Güncel zaman bilgisine ulaşma
data = datetime.datetime.now()
month = data.month
day = data.day

#Güncel zamanı kontrol etme
if MY_MONTH == month and MY_DAY == day:

    #Mesaj gönderme
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Hello Ali\n\nHappy Birthday"
        )