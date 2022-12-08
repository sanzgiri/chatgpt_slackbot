import threading
from revChatGPT.revChatGPT import Chatbot
from flask import Flask, json, request
import requests

# Slack OAuth Access Token
# slack_token = "<your-bot-user-oauth-token>"
# response_url = "<your-incoming-webhook-url>"

config = {
    "email": "<your email>",
    "password": "<your password>",
    "Authorization": "<API-KEY>",
    "session_token": "<your session token>",
}

chatbot = Chatbot(config, conversation_id=None)

# Initialize the Flask object which will be used to handle HTTP requests
# from Slack
app = Flask(__name__)


@app.route("/chatgpt", methods=["POST"])
def chatgpt_handler():

    data = request.form.get("text")
    channel = request.form.get("channel_id"),

    # starting a new thread for doing the actual processing
    x = threading.Thread(
        target=sub_chatgpt,
        args=[data, channel])
    x.start()

    return "Contacting OpenAI.... please wait (can take  ~30 sec)"


def sub_chatgpt(data, channel):

    message = chatbot.get_chat_response(data)['message']

    payload = {"token": slack_token,
               "channel": channel,
               "text": message}

    requests.post(response_url,
                  json.dumps(payload))


# Run on local port 3000
if __name__ == "__main__":
    app.run(port=3000, debug=True)
