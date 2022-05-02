from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/index.html', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


app.run(host='0.0.0.0', port='5001', debug=True)
