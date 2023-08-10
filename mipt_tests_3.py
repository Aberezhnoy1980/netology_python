# ticket 3

def task16(): 
    print("5" * 3 * 2 % 1)

def task17():
    if 5 < 3 and 10 < 12:
        print("True")
    else:
        print("False")

def task18():
    a = [1, 2, 3]
    b = a
    a.append(4)
    print(b)

def task19(a, b):
    x = 0
    for i in range(a, b):
        x += i
    print(x)

def task20(a, b):
    def add_numbers(x, y):
        return x + y
    
    result = add_numbers(a, b)
    print(result)

def task21(x, y):
    if x > 2 or y < 5:
        print("At least one condition is true")
    else:
        print("Both conditions aren't run") 

def task22():
    numbers = [1, 2, 3, 4, 5]
    print(numbers.pop())
    print(numbers[len(numbers) - 1])
    print(numbers[3])
    print(numbers[-1])

def task23(at, to, step):
    for i in range(at, to, step): 
        print(i)

def task24():        
    numbers = []    
    numbers.append(float(input("Enter first number: ")))
    numbers.append(float(input("Enter second number: ")))
    numbers.append(float(input("Enter third number: ")))

    print(sum(numbers) / len(numbers))
    
