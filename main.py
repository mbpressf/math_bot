import telebot

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.from_user.id, 'Здарова, чё помощь нужна? напиши /start')
    bot.send_message(message.from_user.id, """Формула: s = 2 * v1*v2
                    sum = v1+v2
                    s/sum""")
    v1 = bot.send_message(message.from_user.id, 'Напиши два числа через запятую: ')
    bot.register_next_step_handler(v1, sosi)



def sosi(mes):
    v2 = mes.text
    v2 = v2.split(',')
    s = 2 * int(v2[0]) * int(v2[1])
    bot.send_message(mes.chat.id, s / (int(v2[0]) + int(v2[1])))








if __name__ == "__main__":
    bot.polling()
