import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'LazyDeveloper'

os.system("git clone https://Priyanshu1057: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@github.com/Priyanshu1057/Doremonv2 okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
