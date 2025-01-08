#Toplama işlevi oluşturma 
def add(n1, n2):
    return n1 + n2

#Çıkarma işelvi ouşturma
def subtract(n1, n2):
    return n1 - n2

#Çarpma işlevi oluşturma
def multiply(n1, n2):
    return n1 * n2

#Bölme işlevi oluşturma 
def divide(n1, n2):
    return n1 / n2

#Üs alma işlevi oluşturma
def exponential(n1, n2):
    return n1 ** n2

#Hesap makinesinde yapılabilecek işlevlerin sembollerinin bulunduğu sözlük
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": exponential
}

#Hesap makinesi işlevi
def calculator():

    #Kullanıcıdan sayı girişi isteme
    num1 = float(input("What's the first number?: "))

    #İşlevlerin sembollerini yazdırma
    for symbol in operations:
        print(symbol)

    #Döngü kontrol değişkeni
    should_continue = True

    #Hesap makinesini döngüye sokma
    while should_continue:

        #Kullanıcıdan yapılcak işevi seçmesini isteme 
        operation_symbol = input("Pick an operation: ")

        #Kullanıcıdan ikinci sayı girişini isteme 
        num2 = float(input("What's the next number?: "))

        #Sembol anahtarını kullanarak değerine ulaşma ve değişkene kaydetme 
        calculation_function = operations[operation_symbol]

        #Giriş yapılan sayıları işleve vererek sonucu hesaplama
        answer = calculation_function(num1, num2)

        #Sonucu kullanıcıya bildirme 
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        #İşleme devam edilip edilmeyeceğini öğrenme
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            #İlk sayı sonuç olur
            num1 = answer
        else:
            #İşlem sona erer
            should_continue = False
            calculator()

#Hesap makinesi işlevini çağırma 
calculator()