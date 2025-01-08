#Gerekli kütüphanelerin içe aktarılması
import requests
import datetime
import smtplib
import time

#Kullanıcı bilgileri
MY_EMAIL = "alialcan122@gmail.com"
MY_PASSWORD = "bwboejovjlpzalya"
MY_LAT = 51.507351
MY_LONG = -0.127758

#ISS ile kullanıcının konumunu karşılaştırma
def is_iss_overhead():

    #ISS bilgilerine ulaşma
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    #ISS konumunu kaydetme
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Konumunuz ISS konumunun +5 veya -5 derece içinde.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

#Kullanıcının yaşadığı bölgedeki gün doğumunu ve batımını karşılaştırma
def is_night():

    #Kullanıcının konum bilgileri
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    #Kullanıcının gün doğum ve batım bilgilerini kaydetme
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    #Güncel saat bilgisine ulaşma
    time_now = datetime.datetime.now().hour

    #Güncel saat ile gün doğum ve batım bilgilerini karşılaştırma 
    if time_now >= sunset or time_now <= sunrise:
        return True

#Kullanıcıya email ile bilgilendirme
while True:

    time.sleep(60)
    if is_iss_overhead() and is_night():

        connection = smtplib.SMTP("smtp.gmail.com", port=587")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )