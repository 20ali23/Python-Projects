#Facebook veri liste sözlüğü oluşturma
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

#Toplam beğeni sayısı oluşturma
total_likes = 0

#Sözlük için döngü oluşturup toplam beğeni sayısını hesaplama
for post in facebook_posts:
    #Toplam beğeni sayısına beğeni sayısını ekleme
    try:
        total_likes += post['Likes']
    #Beğeni yoksa sıfır kabul etme
    except KeyError:
        post['Likes'] = 0

#Beğeni sayısını yazdırma
print(total_likes)