def task01():
    print(
        input("Enter date: "), 
        input("Enter a task description: "))
    
# task01()

def task02(tries):
    lst = []
    for i in range(0, tries):
        lst.append(input("Enter date: "))
        lst.append(input("Enter a task description: "))
    print()    
    for j in range(0, len(lst), 2):
        print(lst[j], lst[j + 1])
        
# task02(3)

def task03(tries):
    sheduler = {}
    for i in range(0, tries):
        key = input("Enter date: ")
        sheduler[key] = input("Enter a task description: ")
        
    print(sheduler)
    
task03(3)