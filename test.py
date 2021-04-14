import aichatbot as bot

filenames = {
    "intents": "./data/basic_intents.json",
    "dir": "dumps"
}

bot_model = bot.Create(filenames, technique="bow")
bot.start(bot_model)
