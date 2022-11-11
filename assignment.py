def average(numbers:list| tuple):
    sum = 0
    for i in numbers:
        sum = sum + i
    average = sum / len(numbers)
    print(average)

def max(numbers: list|tuple):
    max = numbers[0]
    for i in range(len(numbers)):
        if max < numbers[i]:
            max = numbers[i]
    print(max)

def min(numbers: list|tuple):
    min = numbers[0]
    for i in range(len(numbers)):
        if min > numbers[i]:
            min = numbers[i]
    print(min)

def cuberoot(number):
    print(number**(1/3))

def power(number, exponent):
    print((number)**exponent) 

def squareroot(number):
    print(number**(1/2))

def sum(numbers:list | tuple):
    sum = 0
    for i in numbers:
        sum = sum + i
    print(sum)

def root(numbers, root):
    print(numbers**(1/root))

