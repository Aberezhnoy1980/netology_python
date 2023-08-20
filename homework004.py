import telebot

token = "6483950027:AAHt8F-S-72ynmCvTF1xTYiBfhQv8xGR_pQ"

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, "Вах! Я тебя узнал! Ты в химках деревянными херами торговал!")


bot.polling(none_stop=True)