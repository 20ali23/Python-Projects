import random
from hangman_words import word_list                                  
from hangman_art import logo                                           

#Kelime havuzundan rastgele kelime seçildi
chosen_word = random.choice(word_list)            
#Seçilen kelimenin uzunluğu hesaplandı
word_length = len(chosen_word)                       

#While döngüsü için konrol değişkeni ve can sayısı oluşturuldu
end_of_game = False                                      
lives = 6

#Logo yazdırıldı
print(logo)                                                                          

#Seçilen kelime sayısı kadar _ oluşturuldu
display = []                                                     
for _ in range(word_length):                                                  
    display += "_"                                                  
    
#Oyunu döngüye sokma
while not end_of_game:
    
    #Kullanıcıdan harf tahmini istendi
    guess = input("Guess a letter: ").lower()                                        

    #Önceden tahmin edilen harf olup olmadığını kontrol eder
    if guess in display:
        print(f"You've already guessed {guess}")

    #Kelimedki harflerin konumuna ulaşır
    for position in range(word_length):
        letter = chosen_word[position]                                               

        #Tahmin edilen harf kelimedeki ile aynı mı eğer aynıysa _ ile harfi değiştirir
        if letter == guess:                                                     
            display[position] = letter                  

    #Tahmin edilen harfin kelimenin içinde olup olmadığı kontrol eder
    if guess not in chosen_word:                                                     
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        #Can sayısını bir azaltma
        lives -= 1                           
        #Can sayısı sıfır olursa oyucu kaybetti
        if lives == 0:                                                               
            end_of_game = True
            print("You lose.")

    #Strig haline çevirme
    print(f"{' '.join(display)}")                                                    

    #Bütün kelimeler tahmin edilmişse oyuncu oyunu kazandı
    if "_" not in display:                                                   
        end_of_game = True                  
        print("You win.")

    #Kalan can sayısına göre adamın durumlarını yazdırılır
    from hangman_art import stages                                  
    print(stages[lives])                                                             