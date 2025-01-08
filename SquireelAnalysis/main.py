#Pandas kütüphanesini içe aktarma
import pandas

#Kullanılacak csv dosyasını okuyup kaydetme
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#Renklerin sayısını hesaplama
grey_squireels_count = len(data["Primary Fur Color"] == "Gray")
red_squireels_count = len(data["Primary Fur Color"] == "Red")
black_squireels_count = len(data["Primary Fur Color"] == "Black")

#Renk ismi ve sayısı için sözlük oluşturma
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squireels_count, red_squireels_count, black_squireels_count]
}

#Tablo oluşturma
df = pandas.DataFrame(data_dict)

#Dosyaya yazıp kaydetme
df.to_csv("squirell_count.csv")