#Soru sınıfı oluşturup girdi olarak text ve answer verme
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer