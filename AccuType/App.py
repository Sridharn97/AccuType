from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

leaderboard = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_result', methods=['POST'])
def save_result():
    data = request.get_json()
    wpm = data.get('wpm')
    accuracy = data.get('accuracy')

    if wpm is not None and accuracy is not None:
        leaderboard.append({'wpm': wpm, 'accuracy': accuracy})
        leaderboard.sort(key=lambda x: x['wpm'], reverse=True)
        return jsonify({'status': 'success'}), 200
    return jsonify({'status': 'error', 'message': 'Invalid data'}), 400

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    return jsonify(leaderboard[:10]), 200

if __name__ == '__main__':
    app.run(debug=True)
