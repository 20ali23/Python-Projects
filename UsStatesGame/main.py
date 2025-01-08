#Gerekli kütüphanelerin içe aktarılması 
import turtle
import pandas

#Ekran nesnesi oluşturma 
screen = turtle.Screen()
#Pencere adı verme 
screen.title("U.S. States Game")
#TurtleScreen'in şekil listesine kaplumbağa şeklini ekleme
screen.addshape("blank_states_img.gif")
#Kaplumbağa şekli olarak resmi verme
turtle.shape("blank_states_img.gif")

#Veri setini okuyup kaydetme
data = pandas.read_csv("50_states.csv")
#Liste haline getirme
all_states = data.state.to_list()

#Boş liste oluşturma
guessed_states = []
#Tahmin edilen eyalet sayısı 50'den küçük ise
while len(guessed_states) < 50:
    #Kullanıcıdan eyalet girişi isteme ve pencere bilgileri
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    #Oyundan çıkış yapma
    if answer_state == "Exit":
        #Kullanıcının bilemediği eyaletleri listeye ekleme
        missing_states = [state for state in all_states if state not in guessed_states]
        #DataFrame formatına getirme
        new_data = pandas.DataFrame(missing_states)
        #Csv olarak kaydetme 
        new_data.to_csv("states_to_learn.csv")
        break

    #Giriş yapılan eyaletin liste de olup olmadığını kontrol etme
    if answer_state in all_states:
        #Listeye ekleme
        guessed_states.append(answer_state)
        #Kaplumbağa nesnesi oluşturma
        t = turtle.Turtle()
        #Kaplumbağayı görünmez yapma
        t.hideturtle()
        #Kalemi kaldırma
        t.penup()
        #Kullanıcı girişi veri setinde varsa olduğu satıra ulaşma
        state_data = data[data.state == answer_state]
        #Kaplumbağayı koordinata taşıma
        t.goto(int(state_data.x), int(state_data.y))
        #Eyalet ismini yazma 
        t.write(answer_state)