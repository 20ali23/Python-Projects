#Harf listesi oluşturuldu
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Kullanıcın isteğine göre şifreleme ya da şifre çözme işlemi için fonksiyon oluşturduk
def caesar(start_text, shift_amount, cipher_direction):

  #Boş değişken oluşturma
  end_text = ""

  #Yapılacak işlem kod çözme ise
  if cipher_direction == "decode":
    shift_amount *= -1

  #Şifrelenecek mesajı döngüye sokma
  for char in start_text:
    #Mesajdaki harfi öğrenme
    if char in alphabet:
      #Harfin konumunu öğrenme
      position = alphabet.index(char)
      #Kaydırma poziyonunu ayarlama
      new_position = position + shift_amount
      #Yeni harfi değişkene ekleme
      end_text += alphabet[new_position]

    #Eğer harf dışında bir şey varsa onu olduğu gibi değişkene ekler
    else:
      end_text += char

  #Şifrelenmiş mesajı kullanıcıya bildirme
  print(f"Here's the {cipher_direction}d result: {end_text}")

#Oyunu döngüye sokma
should_end = False
while not should_end:

  #Hangi işlemin yapılacağını öğrenme
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

  #Kullanılacak mesajı öğrenme
  text = input("Type your message:\n").lower()

  #Kaydırma miktarını öğrenme
  shift = int(input("Type the shift number:\n"))

  #Kullanıcı eğer kaydırma miktarı için büyük bir sayı girerse onu harf sayısına göre modunu alıp kalanını bulur
  shift = shift % 26

  #Şifreleme işlevini çağırma
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  #Oyunun devam edilip edilmemesine karar verme
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")