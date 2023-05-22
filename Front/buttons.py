import telebot

############### Кнопки ################
btnBuild = telebot.types.KeyboardButton("🖥 Собрать ПК")
btnModes = telebot.types.KeyboardButton("📄 Моды")
btnModeFirst = telebot.types.KeyboardButton("🥇 Лучший")
btnModeRandom = telebot.types.KeyboardButton("🎲 Рандом")
btnSettings = telebot.types.KeyboardButton("⚙️ Настройки")
btnNVIDIA = telebot.types.KeyboardButton('NVIDIA')
btnAMD = telebot.types.KeyboardButton('AMD')
btnIntel = telebot.types.KeyboardButton('Intel')
btnCPU = telebot.types.KeyboardButton('🧠 CPU')
btnGPU = telebot.types.KeyboardButton('🖥 GPU')
btnANY = telebot.types.KeyboardButton('Любой')
btnGaming = telebot.types.KeyboardButton("🎮 Гейминг")
btnWorking = telebot.types.KeyboardButton("💻 Работа")
btnGraphics = telebot.types.KeyboardButton("🎥 Графика")
btnMenu = telebot.types.KeyboardButton("Меню")

btnSum1 = telebot.types.KeyboardButton("50000")
btnSum2 = telebot.types.KeyboardButton("100000")
btnSum3 = telebot.types.KeyboardButton("150000")

############### Пресеты кнопок ################
markupPrices = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
markupPrices.add(btnSum1, btnSum2, btnSum3)

markupMain = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
markupMain.add(btnBuild, btnSettings, btnModes)

markupBuildCFG = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
markupBuildCFG.add(btnGaming, btnGraphics, btnWorking)

markupModes = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
markupModes.add(btnModeFirst, btnModeRandom)

markupSettings = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
markupSettings.add(btnCPU, btnGPU, btnMenu)

markupSettingsCPU = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
markupSettingsCPU.add(btnIntel, btnAMD, btnANY)

markupSettingsGPU = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
markupSettingsGPU.add(btnNVIDIA, btnAMD, btnANY)