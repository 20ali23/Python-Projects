#Gereki kütüphanelerin içe aktarılması
from bs4 import BeautifulSoup
import requests

#Veri çekeceğimiz internet adresi
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movie = response.text
soup = BeautifulSoup(movie, "html.parser")

#H3 etiketlerini bulma
title = soup.find_all(name="h3", class_="title")

#Çektiğimiz verileri yeni açtığımız txt dosyasına yazma
with open("movies.text", mode="w", encoding="utf-8") as file:
    for i in title[::-1]:
        mov = i.getText()
        file.write(f"{mov}\n")