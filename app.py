from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from flask import jsonify



app = Flask(__name__)

line_bot_api = LineBotApi('M4R/8GWbSSc/VlD/ZbkvZ1+WW8gPi++NdUViiD0my8WkdFgEEr+x+J/02Out44cFU6dtB9qTeSrcNiUZ2C2SVJFCbtL71CByUHMPfSsl5KLFPTepZlwmLjm1uHT4RFJ+i4tJj+gunrqRINIlMPvNTwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('62f6c93485270390dabedef8217d4654')

@app.route("/", methods=['GET'])
def main():
    return "Hello World!"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    #print(body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #print("Good")
    # line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Hello World!'))
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
