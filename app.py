from flask import Flask, jsonify, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

# bot = ChatBot("Candice")
# bot.set_trainer(ListTrainer)
# bot.train(['What is your name?', 'My name is Candice'])
# bot.train(['Who are you?', 'I am a bot' ])
# bot.train(['Do created you?', 'Tony Stark', 'Sahil Rajput', 'You?'])
# bot.set_trainer(ChatterBotCorpusTrainer)
# bot.train("chatterbot.corpus.english")

@app.route("/",methods=["GET"])
def index():
    return render_template("home.html")


def get_response(user_text):
    if user_text=="hii":
        return "hello"
    if user_text=="how are you?":
        return "fine"
    if user_text=="Can I ask you a question?":
        return "yes of course"
    else:
        return "Still learning, sorry!"

@app.route("/get",methods=["GET"])
def get_bot_response():
    userText = request.args.get('msg')
    return str(get_response(userText))



if __name__ == '__main__':
    app.run(debug=True)
