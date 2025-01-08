#Tkinter kütüphanesini içe aktarma
from tkinter import *

#Butona tıklama yapılınca hesaplama yapacak işlev
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")

#Tkinter sınıfından nesne oluşturma
window = Tk()
#Pencere adı
window.title("Miles to Kilometer Converter")
#Dolgu ekleme
window.config(padx=20, pady=20)

#Girdi alma kutusu yerleştirme ve ayarları
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

#miles etiketi yerleştirme ve ayarları
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

#is equal etiketi yerleştirme ve ayarları
is_equal_label = Label(text="is equal label")
is_equal_label.grid(column=0, row=1)

#Sonuçu etiketi yerleştirme ve ayarları
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

#Kilometre etiketi yerleştirme ve ayarları
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

#Buton yerleştirme ve ayarları
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()