#Pandas kütüphanesini içe aktarma
import pandas

#Kullanılacak csv verisini okuyup data değişkenine kaydetme
data = pandas.read_csv("nato_phonetic_alphabet.csv")

#Veri dosaysını sözlüğe çevirme
phonetic_dict = {row.letter: row.code for(index, row) in data.iterrows()}

#Kullanıcıdan kelime girişi alma
word = input("Enter a word: ").upper()

#Girdi kelimesinin nata alphabet karşılığını bulup listeye ekler
output = [phonetic_dict[letter] for letter in word]

#Sonucu kullanıcıya bildirme
print(output)