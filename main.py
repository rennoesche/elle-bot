# import modules from ext. module on python
import os
import requests
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv

gpt_url = os.getenv("URL_GPT")
tg_api = os.getenv("TELEGRAM_BOT_TOKEN")
gpt_api = os.getenv("GPT_API_KEY")

# main function for sending messages to chatGPT
def send_message_to_chatgpt(message):
    # define the url for send and get response
    # this function from official openAI website
    #  url = "https://api.openai.com/v1/chat/completions"
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "system", "content": "You are a bot."}, {"role": "user", "content": message}],
    }
    headers = {
        # change YOUR_GPT_API to your own GPT API
        "Authorization": f"Bearer {gpt_api}",
        "Content-Type": "application/json",
    }
    response = requests.post(gpt_url, json=payload, headers=headers)
    data = response.json()
    return data["choices"][0]["message"]["content"]

# make /gpt command
def gpt(update, context):
    message = update.message
    botm = send_message_to_chatgpt(message.text)
    message.reply_text(botm)

# funct /start
def start(update, context):
    update.message.reply_text("Hello there, blah blah blah. Tehe~")

# function for running bot
def main():
    # change YOUR_API_TG to your own telegram bot API
    updater = Updater(tg_api, use_context=True)


    # handler for command
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("gpt", gpt))

    # running bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
