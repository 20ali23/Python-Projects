#İstek kütüphanesini içe aktarma
import requests

#Uluslar Arası Uzay istasyonunun internet adresine dokunma
response = requests.get(url="http://api.open-notify.org/iss-now.json")
#İstisna yakalama
response.raise_for_status()

#Veriyi json formatında ki değişkene kaydetme
data = response.json()

#Konumu enlem ve boylam olarak kaydetme
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

#Konumu tuple dönüştürme
iss_position = (longitude, latitude)

#Konumu yazdırma
print(iss_position)