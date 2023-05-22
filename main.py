import Back.fnc as fnc
import Front.buttons as ui
import telebot
import os

token = '6293487861:AAGDY7-kNgR1tzWpyp2SJDBTOsHQJkOa0_M' #t.me/buildYourPC_bot
bot = telebot.TeleBot(token)

print('BOT STARTED')

@bot.message_handler(commands=['start', 'info', 'help'])
############### Инициализация /start ################
def start(message):
    bot.send_message(message.chat.id, fnc.init(message), reply_markup=ui.markupMain)
    

@bot.message_handler(content_types=['text'])
############### Проверка ввода ################

def text(message):
    if message.text == ui.btnBuild.text:
        msg = bot.send_message(message.chat.id, 'Укажи нужную цену без пробелов и точек или выбирай из кнопок внизу', reply_markup=ui.markupPrices)
        bot.register_next_step_handler(msg, set_priceStep)
    elif message.text == ui.btnModes.text:
        msg = bot.send_message(message.chat.id, 'Выберите режим', reply_markup=ui.markupModes)
        bot.register_next_step_handler(msg, setMode)
    elif message.text == ui.btnSettings.text:
        msg = bot.send_message(message.chat.id, 'Выберите комплектующее', reply_markup=ui.markupSettings)
        bot.register_next_step_handler(msg, setSettings)
    else:
        bot.send_message(message.chat.id, 'Извини, я тебя не понимаю, используй /help для помощи или /start для кнопок')

############### Режимы ################
def setMode(message):
    try:
        if not os.path.exists(f'{os.getcwd()}\\userdata\\{message.chat.id}'):
            os.makedirs(f'{os.getcwd()}\\userdata\\{message.chat.id}')
        with open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\mode.txt', 'w+') as file:
            if message.text == ui.btnModeFirst.text:
                file.write('first')
                bot.send_message(message.chat.id, f'Режим: {ui.btnModeFirst.text}', reply_markup=ui.markupMain)
                file.close()
            else:
                file.write('random')
                bot.send_message(message.chat.id, f'Режим: {ui.btnModeRandom.text}', reply_markup=ui.markupMain)
                file.close()
    except Exception as e:
        print(f'[{message.chat.id}] Error with setMode({e})')

############### Настройки ################
def setSettings(message):
    try:
        if message.text == "/start" or message.text == ui.btnMenu.text:
            bot.send_message(message.chat.id, 'ОК', reply_markup=ui.markupMain)
        elif message.text == ui.btnCPU.text:
            msg = bot.send_message(message.chat.id, 'Выберите бренд', reply_markup=ui.markupSettingsCPU)
            bot.register_next_step_handler(msg, setSettingsCPU)
        else:
            msg = bot.send_message(message.chat.id, 'Выберите бренд', reply_markup=ui.markupSettingsGPU)
            bot.register_next_step_handler(msg, setSettingsGPU)
    except Exception as e:
        print(f'[{message.chat.id}] Error with settings({e})')

def setSettingsCPU(message):
    try:
        open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\cpu.txt', 'w').write(message.text)
        msg = bot.send_message(message.chat.id, 'Готово. Выберите комплектующее', reply_markup=ui.markupSettings)
        bot.register_next_step_handler(msg, setSettings)
    except Exception as e:
        print(f'[{message.chat.id}] Error with set CPU({e})')
        bot.send_message(message.chat.id, 'Что то пошло не так', reply_markup=ui.markupMain)

def setSettingsGPU(message):
    try:
        open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\gpu.txt', 'w').write(message.text)
        msg = bot.send_message(message.chat.id, 'Готово. Выберите комплектующее', reply_markup=ui.markupSettings)
        bot.register_next_step_handler(msg, setSettings)
    except Exception as e:
        print(f'[{message.chat.id}] Error with set GPU({e})')
        bot.send_message(message.chat.id, 'Что то пошло не так', reply_markup=ui.markupMain)

############### Запрос данных ################
def set_priceStep(message):
    try:
        if not os.path.exists(f'{os.getcwd()}\\userdata\\{message.chat.id}'):
            os.makedirs(f'{os.getcwd()}\\userdata\\{message.chat.id}')
        with open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\price.txt', 'a+') as f:
            f.write(message.text.strip())
            f.close()
        msg = bot.send_message(message.chat.id, 'Ок, определимся для чего тебе нужен ПК', reply_markup=ui.markupBuildCFG)
        bot.register_next_step_handler(msg, set_cfgStep)
    except Exception as e:
        print(f'[{message.chat.id}] Error with price set({e})')
        bot.send_message(message.chat.id, 'Упс, вы ввели не число')

def set_cfgStep(message):
    try:
        with open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\cfg.txt', 'a+') as f:
            if message.text == ui.btnGaming.text:
                f.write("Gaming")
            elif message.text == ui.btnGraphics.text:
                f.write("Graphics")
            elif message.text == ui.btnWorking.text:
                f.write("Working")
            else:
                bot.send_message(message.chat.id, 'Извини, я тебя не понимаю', reply_markup=ui.markupMain)
                f.close()
            f.close()
    except Exception as e:
        bot.send_message(message.chat.id, 'Что-то пошло не так', reply_markup=ui.markupMain)
        print(f'[{message.chat.id}] Error with set cfg({e})')

    try:
        bot.send_message(message.chat.id, fnc.priceCFG(message), reply_markup=ui.markupMain)
    except Exception as e:
        bot.send_message(message.chat.id, 'Что-то пошло не так', reply_markup=ui.markupMain)
        print(f'[{message.chat.id}] Error with price predict({e})')

    try:
        bot.send_message(message.chat.id, fnc.build(message), parse_mode='Markdown')
    except Exception as e:
        bot.send_message(message.chat.id, f'Кажется для данной цены нет сборки, попробуйте увеличить бюджет({e})', reply_markup=ui.markupMain)

    try:
        os.remove(f'{os.getcwd()}\\userdata\\{message.chat.id}\\cfg.txt')
        os.remove(f'{os.getcwd()}\\userdata\\{message.chat.id}\\price.txt')
    except Exception as e:
        print(f'[{message.chat.id}] Error with delete cfg and price({e})')
    

bot.polling(non_stop=True)