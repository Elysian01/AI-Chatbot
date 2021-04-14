import aichatbot as bot

filenames = {
    "intents": "./data/basic_intents.json",
    "dir": "dumps"
}

bot_model = bot.CreateBot(filenames, technique="bow")
bot.start_bot(bot_model)
