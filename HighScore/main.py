#Kullanıcıdan score girişi alma ve bunu listeye çevirme
student_scores = input("Input a list of student scores ").split()

#Listedeki score değerlerini int türüne çevirme
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

#Toplam değeri oluşturma
highest_score = 0

#Listedeki en büyük değeri bulma
for score in student_scores:
  if score > highest_score:
    highest_score = score
      
#Sonucu kullanıcıya bildirme
print(f"The highest score in the class is: {highest_score}")