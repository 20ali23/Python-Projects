#Mesaj oluşturma
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

#Mesajı listeye çevirme
sentence_list = sentence.split()

#For ile üzerinden tek tek geçerek uzunluğunu hesaplayıp yeni sözlüğe ekler
result = {letter: len(letter) for letter in sentence_list}

#Sonucu kullanıcıya bildirme
print(result)