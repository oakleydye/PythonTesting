number = 20
num1 = 0
num2 = 1
nextNum = 0
i = 0

while i < number:
    print(num1)
    nextNum = num1 + num2
    num1 = num2
    num2 = nextNum
    i += 1
