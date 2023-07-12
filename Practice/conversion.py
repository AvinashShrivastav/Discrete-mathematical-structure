def convertTo(number, base):
    Num = []
    while (number >= base):
        r = number % base 
        Num = [r] + Num
        number = int(number/base)
    Num = [number] + Num

    return Num

print(convertTo(1025,2))