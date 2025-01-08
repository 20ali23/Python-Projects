#Kullanıcıdan boy girişi alma
student_heights = input("Input a list of student heights. ").split()

#Boy girişlerini int türüne çevirme
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

#Öğrenci boyları için toplam değeri oluşturma
total_heights = 0

#Öğrenci boylarını toplama
for student in student_heights:
  total_heights += student

#Öğrenci sayısı için oplam değeri oluşturma
number_of_students = 0

#Öğrenci sayısını oluşturma
for student in student_heights:
  number_of_students += 1

#Liste ortalamasını hesaplama
avarge_height = round(int(total_heights) / int(number_of_students))     

#Sonucu kullanıcıya bildirme
print(avarge_height)