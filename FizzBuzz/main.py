#Yüze kadar aralık oluşturma
for i in range(1, 101):
    
    #Sayının 3 ve 5 tam bölünüp bölünmediğini kontrol etme
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
        
    #Sayının 5 tam bölünüp bölünmediğini kontrol etme
    elif i%5 == 0:
        print("Buzz")
        
    #Sayının 3 tam bölünüp bölünmediğini kontrol etme
    elif i%3 == 0:
        print("Fizz")
        
    else:
        print(i)