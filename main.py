import functions as func
import telebot
import os

token = '6293487861:AAGDY7-kNgR1tzWpyp2SJDBTOsHQJkOa0_M' #t.me/buildYourPC_bot
bot = telebot.TeleBot(token)

btnBuild = telebot.types.KeyboardButton("🖥 Собрать ПК")
btnModes = telebot.types.KeyboardButton("📄 Моды")
btnModeFirst = telebot.types.KeyboardButton("🥇 Лучший")
btnModeQueue = telebot.types.KeyboardButton("🔎 Очередь")
btnModeRandom = telebot.types.KeyboardButton("🎲 Рандом")
btnSettings = telebot.types.KeyboardButton("⚙️ Настройки")
btnGaming = telebot.types.KeyboardButton("🎮 Гейминг")
btnWorking = telebot.types.KeyboardButton("💻 Работа")
btnGraphics = telebot.types.KeyboardButton("🎥 Графика")

btnSum1 = telebot.types.KeyboardButton("50000")
btnSum2 = telebot.types.KeyboardButton("100000")
btnSum3 = telebot.types.KeyboardButton("150000")
markupPrices = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
markupPrices.add(btnSum1, btnSum2, btnSum3)

markupMain = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
markupMain.add(btnBuild, btnSettings, btnModes)

markupBuildCFG = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
markupBuildCFG.add(btnGaming, btnGraphics, btnWorking)

markupModes = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
markupModes.add(btnModeFirst, btnModeQueue, btnModeRandom)

print('BOT STARTED')

@bot.message_handler(commands=['start'])
def start(message):
    try:
        if not os.path.exists(f'{os.getcwd()}\\userdata\\{message.chat.id}'):
            os.makedirs(f'{os.getcwd()}\\userdata\\{message.chat.id}')
    except:
        pass
    bot.send_message(message.chat.id, f'Здравствуй, {message.from_user.first_name}! Рады видеть вас в PC Builder – боте, который поможет вам подобрать оптимальную конфигурацию компьютера на любой бюджет.', reply_markup=markupMain)
    if 'name.txt' not in os.listdir(f'{os.getcwd()}\\userdata\\{message.chat.id}'):
        open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\name.txt', 'a+').write(f'Username: {message.from_user.username}\nName: {message.from_user.first_name} {message.from_user.last_name}')
    if 'mode.txt' not in os.listdir(f'{os.getcwd()}\\userdata\\{message.chat.id}'):
        open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\mode.txt', 'a+').write(f'first')


@bot.message_handler(commands=['info', 'help'])
def help_menu(message):
    bot.send_message(message.chat.id, 'Тебе никто не поможет')

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == btnBuild.text:
        msg = bot.send_message(message.chat.id, 'Чтобы собрать компьютер оптимальной конфигурации для твоих потребностей, мне необходимо знать твой бюджет. Пожалуйста, укажи сумму, которую ты готов потратить на компьютер, в формате "XXXXX рублей" (например, "50000 рублей"). После того, как ты укажешь бюджет, я подберу для тебя лучшую возможную конфигурацию ПК в соответствии с твоими предпочтениями.', reply_markup=markupPrices)
        bot.register_next_step_handler(msg, set_priceStep)
        #Сюда запихаем функцию сборки, перед этим спрашиваем нужные данные
    elif message.text == btnModes.text:
        msg = bot.send_message(message.chat.id, 'Выберите режим', reply_markup=markupModes)
        bot.register_next_step_handler(msg, setMode)

    elif message.text == btnSettings.text:
        pass
        #могу организовать настройки, запарно, но идея уже есть
    else:
        bot.send_message(message.chat.id, 'Извини, я тебя не понимаю, используй /help для помощи или /start для кнопок')

def setMode(message):
    if not os.path.exists(f'{os.getcwd()}\\userdata\\{message.chat.id}'):
        os.makedirs(f'{os.getcwd()}\\userdata\\{message.chat.id}')
    with open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\mode.txt', 'w+') as file:
        if message.text == btnModeFirst.text:
            file.write('first')
            bot.send_message(message.chat.id, btnModeFirst.text, reply_markup=markupMain)
            file.close()
        elif message.text == btnModeQueue.text:
            file.write('queue')
            bot.send_message(message.chat.id, btnModeQueue.text, reply_markup=markupMain)
            file.close()
        else:
            file.write('random')
            bot.send_message(message.chat.id, btnModeRandom.text, reply_markup=markupMain)
            file.close()

def set_priceStep(message):
    try:
        if not os.path.exists(f'{os.getcwd()}\\userdata\\{message.chat.id}'):
            os.makedirs(f'{os.getcwd()}\\userdata\\{message.chat.id}')
        with open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\price.txt', 'a+') as f:
            f.write(message.text.strip())
            f.close()
        msg = bot.send_message(message.chat.id, 'Ок, определимся для чего тебе нужен ПК', reply_markup=markupBuildCFG)
        bot.register_next_step_handler(msg, set_cfgStep)
    except Exception as e:
        bot.send_message(message.chat.id, 'Упс, вы ввели не число')

def set_cfgStep(message):
    with open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\cfg.txt', 'a+') as f:
        if message.text == btnGaming.text:
            f.write("Gaming")
        elif message.text == btnGraphics.text:
            f.write("Graphics")
        elif message.text == btnWorking.text:
            f.write("Working")
        else:
            bot.send_message(message.chat.id, 'Извини, я тебя не понимаю', reply_markup=markupMain)
            f.close()
        f.close()


    bld = func.Build(sum_price=int(open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\price.txt', 'r').read()), cfg=open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\cfg.txt', 'r').read())
    bld.set_price()
    bot.send_message(message.chat.id, f'''Расчет цены:
    Материнская плата до {bld.motherboard_price[1]} руб
    Процессор до {bld.cpu_price[1]} руб
    Видеокарта до {bld.gpu_price[1]} руб
    Накопитель до {bld.rom_price[1]} руб
    Оперативная память до {bld.ram_price[1]} руб
    Блок питания до {bld.psu_price[1]} руб
    ''', reply_markup=markupMain)
    try:
        builder = func.Build(sum_price=int(open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\price.txt', 'r').read()),
                             cfg=open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\cfg.txt', 'r').read(),
                             mode=open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\mode.txt', 'r').read())
        builder.set_price()
        builder.build()
        
        bot.send_message(message.chat.id, builder.out())
    except Exception as e:
        bot.send_message(message.chat.id, f'Кажется для данной цены нет сборки, попробуйте увеличить бюджет({e})', reply_markup=markupMain)
    try:
        os.remove(f'{os.getcwd()}\\userdata\\{message.chat.id}\\cfg.txt')
        os.remove(f'{os.getcwd()}\\userdata\\{message.chat.id}\\price.txt')
    except Exception as e:
        print(e)
    

bot.polling(non_stop=True)