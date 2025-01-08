#Satırları oluşturma
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

#map adında liste oluşturma
map = [row1, row2, row3]

#Satırları yazdırma
print(f"{row1}\n{row2}\n{row3}")

#Kullanıcıdan bir pozisyon girmesinin istenmesi
position = input("Where do you want to put the treasure? ")

#Girilen pozisyonun sıfırıncı ve birinci indeksteki değerlerinin kaydedilmesi
horizonal = int(position[0])
vertical = int(position[1])

#İstenilen pozisyona "X" ekleme
map[vertical-1][horizonal-1] = "X"

#Satırları yazdırma
print(f"{row1}\n{row2}\n{row3}")