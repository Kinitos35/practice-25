import telebot


eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
symbol = [" ", ",", ".", "!", "?"]


bot = telebot.TeleBot('7757455927:AAGs5IiUVo3OioXaR2FYIeqPLs3u_-B-NVc')




def chru(chifr, n, l, fraza):
    if l == 'r':
        moch = 32
    if l == 'e':
        moch = 26
    if chifr == 'def':
        n = -n
    result = []
    for i in range(len(fraza)):
        if fraza[i].isalpha():
            if fraza[i] == fraza[i].upper():
                for j in range(moch):
                    if moch == 32:
                        if fraza[i] == rus_upper_alphabet[j]:
                            result.append(rus_upper_alphabet[(j + n) % moch])
                            break
                    if moch == 26:
                        if fraza[i] == eng_upper_alphabet[j]:
                            result.append(eng_upper_alphabet[(j + n) % moch])
                            break
            elif fraza[i] == fraza[i].lower():
                for j in range(moch):
                    if moch == 32:
                        if fraza[i] == rus_lower_alphabet[j]:
                            result.append(rus_lower_alphabet[(j + n) % moch])
                            break
                    if moch == 26:
                        if fraza[i] == eng_lower_alphabet[j]:
                            result.append(eng_lower_alphabet[(j + n) % moch])
                            break
        else:
            result.append(fraza[i])
    return ''.join(result)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот для шифрования и дешифрования текста.\n"
                                      "Выберите язык: английский (e) или русский (r)?")


@bot.message_handler(func=lambda message: message.text.lower() in ['e', 'r'])
def choose_language(message):
    language = message.text.lower()
    bot.send_message(message.chat.id, "Вы выбрали язык: " + ("Английский" if language == 'e' else "Русский") +
                     ".\nТеперь выберите шифрование (ch) или дешифрование (def)?")
    bot.register_next_step_handler(message, choose_action, language)


def choose_action(message, language):
    action = message.text.lower()
    if action not in ['ch', 'def']:
        bot.send_message(message.chat.id, "Пожалуйста, выберите правильное действие: шифрование (ch) или дешифрование (def).")
        bot.register_next_step_handler(message, choose_action, language)
        return
    bot.send_message(message.chat.id, "Введите ключ шифрования (целое число):")
    bot.register_next_step_handler(message, get_key, language, action)


def get_key(message, language, action):
    try:
        key = int(message.text)
        bot.send_message(message.chat.id, "Введите текст для шифрования/дешифрования:")
        bot.register_next_step_handler(message, get_text, language, action, key)
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите целое число для ключа.")
        bot.register_next_step_handler(message, get_key, language, action)


def get_text(message, language, action, key):
    text = message.text
    result = chru(action, key, language, text)
    bot.send_message(message.chat.id, f"Результат:\n{result}")


bot.polling()
