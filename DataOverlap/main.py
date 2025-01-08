#txt dosyayısını açıp listeye çevirme
with open("file1.txt") as file1:
    file_1_data = file1.readlines()

#txt dosyasını açıp listeye çevirme
with open("file2.txt") as file2:
    file_2_data = file2.readlines()

#Kaydedilen dosyaları karşılaştırıp ortak olanları listeye ekler
result = [int(num) for num in file_1_data if num in file_2_data]

#Listeyi yazdırma
print(result)