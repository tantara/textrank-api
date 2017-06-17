from flask import Flask, request, jsonify
from summa import summarizer, keywords

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/summary', methods=['POST'])
def summary():
    content = request.form['content']

    res = dict()
    res['summary'] = summarizer.summarize(content).split("\n")
    res['keywords'] = keywords.keywords(content).split("\n")

    return jsonify(res)