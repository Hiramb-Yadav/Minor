#A Temperature Conversion Porgram

Selection = int(input("Enter number"))
T = int(input("Enter number"))

def CelsiusToFaherenheit(T):
    sol = T*9/5 + 32
    return sol

def FaherenheitToCelsius(T):
    sol = (T-32)*5/9
    return sol

def Conversion(Selection,T):
    if Selection == 1:
        return CelsiusToFaherenheit(T)

    else:
        return FaherenheitToCelsius(T)

ans = Conversion(Selection,T)
print(ans)



