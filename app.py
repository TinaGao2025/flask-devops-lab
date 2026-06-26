import json
import platform
import socket
import time
from flask import Flask, jsonify

app = Flask(__name__)

START_TIME = time.time()

def load_config(path='config.json'):
    with open(path, 'r') as f:
        return json.load(f)

@app.get('/api/health')
def health():
    return jsonify({'status': 'ok'})


@app.get('/api/config')
def config():
    return jsonify(load_config())

@app.get('/api/report')
def report():
    return jsonify({
        'hostname': socket.gethostname(),
        'python_version': platform.python_version(),
        'uptime_seconds': round(time.time() - START_TIME, 2)
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
