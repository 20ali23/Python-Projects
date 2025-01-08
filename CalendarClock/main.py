#Datetime kütüphanesini içe aktarma
import datetime as dt

#Calendar fonksiyonunu oluşturma
def calendar():
    now = dt.datetime.now()

    year = now.year
    month = now.month
    weekday = now.weekday() + 1
    hour = now.hour
    minute = now.minute

    return f"Year:{year}, Month:{month}, Weekday:{weekday}, Time:{hour}:{minute}"

#Fonksiyonu çağırıp sonucu kullanıcıya bildirme
new_calendar = calendar()
print(new_calendar)