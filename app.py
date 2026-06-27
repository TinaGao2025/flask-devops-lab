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

@app.get('/dashboard')
def dashboard():
    config_data = load_config()

    return f"""
    <h1>Application Status Dashboard</h1>
    <ul>
        <li>Status: OK</li>
        <li>Application: {config_data['app_name']}</li>
        <li>Version: {config_data['version']}</li>
        <li>Hostname: {socket.gethostname()}</li>
        <li>Python Version: {platform.python_version()}</li>
        <li>Uptime Seconds: {round(time.time() - START_TIME, 2)}</li>
    </ul>
    """
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
