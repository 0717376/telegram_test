import telebot
# Создаем экземпляр бота
bot = telebot.TeleBot('5197102386:AAEPZSYREmRLnGmLrhxAZOvZwWYnGdGHVcY')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'В твоем сообщении вот сколько букв: ' + len(message.text))
# Запускаем бота
bot.polling(none_stop=True, interval=0)