#Öğrenci not bilgi sözlüğü oluşturma
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

#Boş sözlük oluşturma
student_grades = {}

#Sözlükteki notları karşılaştırıp yorumlayıp boş sözlüğe ekleme
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"

    elif score > 80:
        student_grades[student] = "Exceeds Expectations"

    elif score > 70:
        student_grades[student] = "Acceptable"

    elif score < 70:
        student_grades[student] = "Fail"

#Sözlüğü kullanıcıya bildirme
print(student_grades)