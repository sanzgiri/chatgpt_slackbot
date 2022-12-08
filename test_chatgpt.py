from revChatGPT.revChatGPT import Chatbot

config = {
    "email": "<your email>",
    "password": "<your password>",
    "Authorization": "<API-KEY>",
    "session_token": "<your session token>",
}

chatbot = Chatbot(config, conversation_id=None)

message = chatbot.get_chat_response("Hello World")['message']

print(message)