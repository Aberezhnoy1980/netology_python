# name = input("Enter your name: ")
# print(name)
# checkName = "Alex"

# if name == checkName:
#     print("Hello", name)
# elif name == "Yo":
#     print("Yo, bro")
# elif len(name) < 3:
#     print("Such name is unacceptable")
# else:
#     print("Hello, user")

# print("The end")

tasks = []


def commandHandler(tasks):
    HELP = """
    help - напечатать справку по программе.
    add - добавить задачу в список (название задачи запрашиваем у пользователя).
    show - напечатать все добавленные задачи."""

    run = True
    command = ""
    while run:
        command = input("Enter a command: ")
        if command == "help":
            print(HELP)
        elif command == "show":
            print(tasks)
        elif command == "add":
            addTask(tasks)
        elif command == "exit":
            print("wow!")
            break   
        else:
            print("Command not found")
            break
            
    print("bye, bitches")

def addTask(tasks):
    task = input("Enter a task description: ")
    tasks.append(task)
    print("task added successfully")

commandHandler(tasks)

# x = 1

# while x <= 10:
#     print(x)
#     x += 1
    
#     print(x)
