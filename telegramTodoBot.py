import telebot
import random

token = "6483950027:AAHt8F-S-72ynmCvTF1xTYiBfhQv8xGR_pQ"

bot = telebot.TeleBot(token)

HELP = """
/help - вывестии список досупных команд.
/add - добавить задачу.
/show - показать задачи на дату.
/random - добавить случайную задачу на дату сегодня"""

RANDOM_TASKS = ["Sign up for a course in Netology", "Write Guido (Python founder) a letter", "Feed the cat", "To wash the car"]

tasks = {}

def add_todo(date, task):
        if date in tasks:
            tasks[date].append(task)
        else:
            tasks[date] = [task]

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add", "random_add"])
def add(message):
    message_args_sequence = message.text.split(maxsplit=2)
    command = message_args_sequence[0]
    date = "".lower
    task = ""
    add_todo(date, task)
    if command == "/add":
        if len(message_args_sequence[2]) < 3:
            bot.send_message(message.chat.id, "Task incorrect. Please enter the task descreption conteined more than 3 symbols")
        else:
            date = message_args_sequence[1]
            task = message_args_sequence[2]
            add_todo(date, task)
    elif command == "/random_add":
        date = "today"
        task = random.choice(RANDOM_TASKS)
        add_todo(date, task)
    text = "Task " + task + " added succcessfully on date " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show", "print"])
def show(message):
    message_args_sequence = message.text.split()
    for i in range(1, len(message_args_sequence)):
        date = message_args_sequence[i]
        text = ""
        if date in tasks:
            text = date.upper() + "\n"
            for task in tasks[date]:
                text += "[] " + task + "\n"
        else:
            text = "No tasks at " + date + " found"
        bot.send_message(message.chat.id, text)

bot.polling(non_stop=True)