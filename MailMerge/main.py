#Dosyayı açıp names_file adlı değişkenine kaydetme
with open("./Input/Names/invited_names.txt") as names_file:
    #Text'i liste haline getirme
    names = names_file.readlines()

#Dosyayı açıp letter_file adlı değişkenine kaydetme
with open("./Input/Letters/starting_letter.txt") as letter_file:
    #Dosyayı okuma
    letter_contents = letter_file.read()

    for name in names:
        #Boşlukları kaldırma
        stripped_name = name.strip()
        #[name]'yi stripped_name ile değiştirme
        new_letter = letter_contents.replace("[name]", stripped_name)

        #Dosyayı açıp completed_letter adlı değişkenine kaydetme
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            #new_letter adında txt dosyayısı açma
            completed_letter.write("new_letter.txt")