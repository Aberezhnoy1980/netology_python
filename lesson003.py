import random

# for i in [4, 5, 6]:
#     if i % 2 == 0:
#         print(i)

# def multiply(a, b):
#     print("a =  ", a)
#     print("b =  ", b)
#     result = a * b
#     return result

# c = multiply(3, 5)
# print(c)
# print(multiply(4, 6))

# def print_hello():
#     print("Hello")
#     print("World")

# print_hello()
# print_hello()

# HELP = """
# help - напечатать справку по программе.
# add - добавить задачу в список (название задачи запрашиваем у пользователя).
# show - напечатать все добавленные задачи.
# random - добавить случайную задачу на дату сегодня"""

# RANDOM_TASK = "Sign up for a course in Netology"
# RANDOM_TASKS = ["Sign up for a course in Netology", "Write Guido (Python founder) a letter", "Feed the cat", "To wash the car"]

# tasks = {}

# def add_todo(date, task):
#     if date in tasks:
#         tasks[date].append(task)
#     else:
#         tasks[date] = []
#         tasks[date].append(task)
#     print("Task ", task, " added successfully on date ", date)

# while True:
#     command = input("Enter a command: ")
#     if command == "add":
#         date = input("Enter the due date for the task: ")
#         task = input("Enter a task description: ")
#         add_todo(date, task)
#     elif command == "random":
#         task = random.choice(RANDOM_TASKS)
#         add_todo("today", task)
#     elif command == "help":
#         print(HELP)
#     elif command == "show":
#         date = input("Enter date for view: ")
#         if date in tasks:
#             for task in tasks[date]:
#                 print("- ", task)
#         else:
#             print("no date available")
#     elif command == "exit":
#         print("Thanks for using! Bye!")
#         break
#     else:
#         print("Unknown command!")
#         break

# msg = "/add 31.12.2023 Task description text"
# phrase_part = msg.rstrip.split(maxsplit=2)
# print(phrase_part)

tasks = {"today": ["asd", "dsa"], "tomorrow": ["qwe", "ewq"], "31.12.2023": ["poi", "iop"]}

message = "/show today tomorrow 31.12.2023 February"


def show(message):
    message_args_sequence = message.split()
    for i in range(1, len(message_args_sequence)):
        date = message_args_sequence[i]
        text = ""
        if date in tasks:
            text = date.upper() + "\n"
            for task in tasks[date]:
                text += "[] " + task + "\n"
        else:
            text = "No tasks at " + date + " found"
        print(text)
        
show(message)
