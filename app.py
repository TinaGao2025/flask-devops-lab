import json
from flask import Flask, jsonify

app = Flask(__name__)


def load_config(path='config.json'):
    with open(path, 'r') as f:
        return json.load(f)


@app.get('/api/health')
def health():
    return jsonify({'status': 'ok'})


@app.get('/api/config')
def config():
    return jsonify(load_config())


if __name__ == '__main__':
    app.run(debug=True)
