class MenuItem:
    #Her Menü Öğesini modeller.
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    #Menüyü içeceklerle modeller.
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        #Mevcut menü öğelerinin tüm adlarını döndürür
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        #Belirli bir içecek için menüde ada göre arama yapar. Varsa bu öğeyi döndürür, aksi halde Yok'u döndürür
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")