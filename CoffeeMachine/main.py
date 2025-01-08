#İçeceklerin yapılması için gerekli olan malzeme ve fiyat bilgileri
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

#Makinedeki para ve malzeme bilgisi
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#Kullanılcak malzemelerin yeterli olup olmamasının kontrol edilmesi.
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough water {item}.")
            return False
    return True

#Madeni para girişi hesaplama
def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

#Paranın yeterli olup olmamasının kontrolü ve para üstü bilgisi
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

#Malzemelerin miktarnın makinedeki kaynaktan eksilmesi
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Her is your {drink_name}.")

#Döngüye sokma
is_one = True
while is_one:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    #Makineyi kapatma
    if choice == "off":
        is_one = False

    #Makine içindeki kalan malzemelerin ve paranın raporu
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        #Kullancının istediği içeceği ayarlama
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])