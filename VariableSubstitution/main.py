#Kullanıcıdan A ve B sayı girişi alma
A = input("A: ")
B = input("B: ")

#A ve B sayısını değiştirme 
C = A                             
A = B
B = C

#Değiştirilmiş A ve B sayısını kullanıcıya bildirme mesajı
print("A:" + A)
print("B:" + B)