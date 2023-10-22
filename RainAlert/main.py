#Gerekli kütüphanelerin içe aktarılması
import requests
import smtplib

#Veri çekmek için kullanacağımız adres ve api anahtarı
OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
API_KEY = "c87540b8621c8ba9d5db31d854220fb7"

#Kullanıcı email bilgileri
MY_EMAIL = "alialcan122@gmail.com"
MY_PASSWORD = "uizaixwawhugwiic"

#Parametre bilgileri
weather_params = {
    "lat": 41.013000,
    "lon": 28.974800,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

#Veriyi çekip değişkene kaydetme
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

#12 saat içinde yağmur yağıp yağmayacağını kontrol etme
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

#Yağmur yağışı varsa kullanıcıya mail atma
if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Dikkat Yağmur\n\nDışarı çıkarken şemsiyenizi yanınıza almayı untmayınız.".encode("utf-8")
        )