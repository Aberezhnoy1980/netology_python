HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

todayTasks = []
tomorrowTasks = []
otherTasks = []

run = True

while run:
    command = input("Enter command: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        choice = input("Enter date: ")
        if choice == "today":
            print(todayTasks)
        elif choice == "tomorrow":
            print(tomorrowTasks)
        else:
            print(otherTasks)
    elif command == "add":
        date = input("Enter date: ")
        if date == "today":
            todayTasks.append(input("Enter a task description for today: "))
        elif date == "tomorrow":
            tomorrowTasks.append(input("Enter a task description for tomorrow: "))
        else:
            otherTasks.append(input("Enter a task description: "))
        print("Task added successfully!")
    elif command == "exit":
        print("Thanks for using! Bye!")
        break
    else:
        print("Command unknown")
        run = False
