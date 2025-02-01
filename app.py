from flask import Flask, request
import telegram
from pyngrok import ngrok
public_url = ngrok.connect(5000).public_url
print(f"Webhook URL: {public_url}/webhook")

app = Flask(__name__)

# Token do seu bot
TOKEN = "8063258730:AAFdmf4m-dwhhy5N1GdC6EjMG9IQi-DO168"
bot = telegram.Bot(token=TOKEN)

@app.route("/webhook", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    # Responde à mensagem
    bot.send_message(chat_id=chat_id, text=f"Você disse: {text}")

    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)