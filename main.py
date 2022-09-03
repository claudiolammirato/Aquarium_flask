from flask import Flask, render_template

app = Flask(__name__)

messages = [{'title': 'Aquarium Temperature',
             'content': '28'},
            {'title': 'Room Temperature',
             'content': '20'}
            ]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

app.run(host='0.0.0.0', port=8000)