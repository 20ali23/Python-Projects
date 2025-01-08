#Gerekli kütüphanelerin içe aktarılması
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#Soru havuzumuzdaki soruları soru sınıfını kullanarak listeye ekleme
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

#Kullanıcıya soru sorma
while quiz.still_has_questions():
    quiz.next_question()

#Oyuncuya sonuç bilgisi verme
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")