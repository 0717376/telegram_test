import telebot
# Создаем экземпляр бота
bot = telebot.TeleBot('5389545769:AAH6mJEHBmULp5Bf9eo2JHxCy5HFVvod8ks')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне ИНН контрагента )')

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'сслыка на краткий отчет Контур: ' + f'https://focus-api.kontur.ru/api3/briefReport?key=ZFEmineQeAa7ZmJhvbPQNs1HWuxp7D9gDKyRWmVp&inn={message}&pdf=True')
# Запускаем бота
bot.polling(none_stop=True, interval=0)
