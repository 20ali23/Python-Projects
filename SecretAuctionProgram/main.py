#Gerekli kütüphanelerin içe aktarılması
from replit import clear
from art import logo

#Logo ve karşılama mesajı
print(logo)
print("Welcome to the secret auction program.")

#Boş sözlük oluşturma
bids = {}

#Döngü kontrol değişkeni
bidding_finished = True

#Sözlük içerisinde döngü yapıp en yüksek fiyatı veren kişiyi bulabilmek için fonksiyon oluşturduk
def find_highest_bidder(bidding_record):

  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = int(bidding_record[bidder])
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid} ")

#Oyun döngüye sokma
while bidding_finished:

  #Kullanıcıdan isim girişi alma
  name = input("What is your name?: ")
  #Kullanıcıdan fiyat bilgisi alma
  price = int(input("What's your bid ?: $"))
  #Kullanıcı adını ve fiyatını sözlüğe ekleme
  bids[name] = price
  #Eklenecek isim olup olmadığını öğrenme
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")

  #Eklenecek isim yoksa döngüden çıkıp yüksek fiyat veren kişiyi bildirme
  if should_continue == "no":
    bidding_finished = False
    find_highest_bidder(bids)

  #Eklenecek isim varsa ekranı temizleyip başa dönme
  elif should_continue == "yes":
    clear()