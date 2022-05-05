from flask import Flask, request, render_template, jsonify
from game import game

app = Flask(__name__)

parties = [
    {'id': 1, 'word': 'TUER', 'progression': 'T_E_'}
]

@app.route('/', methods=['GET'])
@app.route('/index.html', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/actions/start_game', methods=['GET'])
def startGame():
    global parties
    partyId = request.args.get('id')

@app.route('/actions/create_game', methods=['POST'])
def createGame():
    global parties
    print('a')

app.run(host='0.0.0.0', port='5001', debug=True)
