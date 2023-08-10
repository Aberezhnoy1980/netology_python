# ticket 1-2

def task15(): 
    print("1-st line\nsecond line")

def task16():
    a = int(input("Enter any integer: "))
    if isinstance(a, int):
        print("true")
    else:
        print("false")

def task17(a, b):
    if a == b:
        return a + b
    else:
        return b - a
    
# print(task17(
#     int(input("Enter a integer: ")), 
#     int(input("Enter b integer: "))))

def task18():
    list1 = [1, 2, 3]
    list2 = ["one", "two", "three"]
    print(list1 + list2)
    
def task19():
    True
    if True:
        print("For condition operator use \"if\" and \"else\"")

def task20():
    instruction = ["add element"]
    instruction.append("use append() function to add element at the end of list")
    print(instruction)

def task21():
    numbers = [1, 2, 3, 4]
    print(numbers[0])
    numbers.reverse()
    print(numbers)
    numbers.clear()
    print(numbers)
    
def task22(at, to):
    for i in range(at, to + 1, 2):
        print(i)
        
task22(0, 6)

def task23():
    lst = [0, 1, 2, 3, 4]
    print(lst)

def task24(lst):
    even_numbers = []
    for i in range(0, len(lst)):
        if  lst[i] % 2 == 0:
            even_numbers.append(lst[i])
            
    print(even_numbers)

task24(lst = [1, 2, 3, 4, 5, 6, 7, 8, 9])