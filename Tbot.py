import telebot
import config

bot = telebot.Telebot(config.TOKEN)
@bot.messange_handler(content_type=["text"])
def My_massage(massage):
	bot.send_message()