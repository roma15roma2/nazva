# Функція перетворення в десятичну систему числення
def anytodec(text, base):  # string, string
    a = 1
    res = 0
    base = int(base)
    for i in reversed(text):
        res += a * int(i)
        a *= base
    return res


# Окрема функція для перетворення з 16-ї системи в 10-чну
def hextodec(text):  # string, return - int
    a = 1
    res = 0
    base = 16
    for i in reversed(text):
        res += a * int(retDEC(i))
        a *= base
    return res


# Function for convert decimal into 10+ base
def dectohex(decnum, base=16):
    templine = ""
    num = int(decnum)
    while num >= base:
        templine += retHEX(num % base)
        num = int(num / base)
    templine += str(retHEX(num))

    return str(templine[::-1])


# Функція для перетворення з формату HEX в інші
def hextoany(text):  # string, read base, return string
    print("В яку систему перевести? Введіть 2-16")
    base = input()
    decNum = hextodec(text)  # переводимо з 10+системи в десятичну
    if int(base) < 11:
        return dectoany(decNum, int(base))  # перетворення в менші за 10-чну системи
    else:
        return dectohex(decNum, int(base))  # перетворення в більші за 10-чну системи


# Функція, що повертає число в форматі HEX
def retHEX(a):  # a - int, return - string
    nums = "0123456789ABCDEF"
    return nums[a]


# Функція, що повертає число в форматі DEC
def retDEC(a):  # a - string, return - int
    nums = "0123456789ABCDEF"
    return nums.find(a)


# Функція для перетворення з 10-чної в менші системи числення
def dectoany(dectext, c=2):  # string, int, return - string
    line = ""
    num = int(dectext)
    while num >= c:
        line += str(num % c)
        num = int(num / c)
    line += str(num)
    return str(line[::-1])


# Для перетворення з будь-якої в іншу с.ч.
def anytoany(num, base):
    print("В яку систему перевести число? Введіть 2-16")
    newbase = int(input())
    decnum = anytodec(num, base)
    if newbase < 11:
        return decto any(str (decnum), newbase)
    else:
        return dectohex(str(decnum), newbase)


# Початок виконання програми
print("Введіть число в форматах")
print("0b1010, 0xA1A, 245x8, 2423 або 'no'")
line = input()

while line != "no":
    if len(line) < 2:
        print(dectoany(line))
    else:
        if line[1] == "b":  # якщо число в бінарному форматі
            num = line.split("b")[1]
            print("В 10-чній системі:")
            print(anytodec(num, 2))
        else:
            if line[1] == "x":  # якщо число в HEX форматі
                num = line.split("x")[1]
                print(hextoany(num))
            else:
                if line[len(line) - 2] == "x" or line[len(line) - 3] == "x":  # якщо число в 3-15 форматі
                    nums = line.split("x")
                    print(anytoany(nums[0], nums[1]))
                else:  # просто 10-чне число
                    print(dectoany(line))

    print("Введіть число для переводу або 'no'")
    line = input()
