from flask import Flask
import os
import datetime
import psutil

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Siddamshetty vaishnavi"  
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")

    process_info = "<br>".join([
        f"{p.info['pid']} {p.info['name']}"
        for p in psutil.process_iter(['pid', 'name'])
    ])

    return f"""
    <h1>System Information</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <h2>Top Output</h2>
    <pre>{process_info}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
