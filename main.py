import functions as f
import telebot

token = '6293487861:AAGDY7-kNgR1tzWpyp2SJDBTOsHQJkOa0_M' #t.me/buildYourPC_bot
bot = telebot.TeleBot(token)

btnBuild = telebot.types.KeyboardButton("🖥 Собрать ПК")
btnHelp = telebot.types.KeyboardButton("📄 Помощь")
btnSettings = telebot.types.KeyboardButton("⚙️ Настройки")
btnGaming = telebot.types.KeyboardButton("🎮 Гейминг")
btnWorking = telebot.types.KeyboardButton("💻 Работа")
btnGraphics = telebot.types.KeyboardButton("🎥 Графика")

markupMain = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
markupMain.add(btnBuild, btnSettings, btnHelp)

markupBuildCFG = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
markupBuildCFG.add(btnGaming, btnGraphics, btnWorking)

print('BOT STARTED')
price = 0
cfg = ''

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Здравствуй, {message.from_user.first_name}! Рады видеть вас в PC Builder – боте, который поможет вам подобрать оптимальную конфигурацию компьютера на любой бюджет.', reply_markup=markupMain)


@bot.message_handler(commands=['info', 'help'])
def help_menu(message):
    bot.send_message(message.chat.id, 'Тебе никто не поможет')

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == btnBuild.text:
        msg = bot.send_message(message.chat.id, 'Чтобы собрать компьютер оптимальной конфигурации для твоих потребностей, мне необходимо знать твой бюджет. Пожалуйста, укажи сумму, которую ты готов потратить на компьютер, в формате "XXXXX рублей" (например, "50000 рублей"). После того, как ты укажешь бюджет, я подберу для тебя лучшую возможную конфигурацию ПК в соответствии с твоими предпочтениями.')
        bot.register_next_step_handler(msg, set_priceStep)
        #Сюда запихаем функцию сборки, перед этим спрашиваем нужные данные
    elif message.text == btnHelp.text:
        bot.send_message(message.chat.id, 'Тебе никто не поможет')
        #Описание бота, наверное
    elif message.text == btnSettings.text:
        pass
        #могу организовать настройки, запарно, но идея уже есть
    else:
        bot.send_message(message.chat.id, 'Извини, я тебя не понимаю, используй /help для помощи или /start для кнопок')

def set_priceStep(message):
    try:
        global price
        price = int(message.text)
        msg = bot.send_message(message.chat.id, 'Ок, определимся для чего тебе нужен ПК', reply_markup=markupBuildCFG)
        bot.register_next_step_handler(msg, set_cfgStep)
    except:
        bot.send_message(message.chat.id, 'Упс, вы ввели не число')

def set_cfgStep(message):
    if message.text == btnGaming.text:
        cfg = 'Gaming'
    elif message.text == btnGraphics.text:
        cfg = 'Graphics'
    elif message.text == btnWorking.text:
        cfg = 'Working'
    else:
        bot.send_message(message.chat.id, 'Извини, я тебя не понимаю')


    bld = f.Build(sum_price=price, cfg=cfg)
    bld.set_price()
    bot.send_message(message.chat.id, f'''Собрать пока что не могу, но выведу расчет цены:
    Материнская плата: {bld.motherboard_price[0]}-{bld.motherboard_price[1]} руб
    Процессор: {bld.cpu_price[0]}-{bld.cpu_price[1]} руб
    Видеокарта: {bld.gpu_price[0]}-{bld.gpu_price[1]} руб
    Накопитель: {bld.rom_price[0]}-{bld.rom_price[1]} руб
    Оперативная память: {bld.ram_price[0]}-{bld.ram_price[1]} руб
    Блок питания: {bld.psu_price[0]}-{bld.psu_price[1]} руб
    ''', reply_markup=markupMain)


bot.polling(non_stop=True)

# bld = f.Build(sum_price=40000, cfg="Gaming")
# bld.set_price()
# print(bld.motherboard_price)
# print(bld.cpu_price)
# print(bld.gpu_price)