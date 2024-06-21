from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# API to get settings
@app.route('/api/settings', methods=['GET'])
def get_settings():
    conn = get_db_connection()
    settings = conn.execute('SELECT * FROM settings').fetchall()
    conn.close()
    return jsonify({'settings': [dict(setting) for setting in settings]})

# API to update settings
@app.route('/api/update', methods=['POST'])
def update_settings():
    setting_name = request.form['setting_name']
    setting_value = request.form['setting_value']

    conn = get_db_connection()
    conn.execute('UPDATE settings SET value = ? WHERE name = ?', (setting_value, setting_name))
    conn.commit()
    conn.close()

    return jsonify({'status': 'success'})

# API to generate invite link
@app.route('/api/generate_invite', methods=['POST'])
def generate_invite():
    client_id = "YOUR_DISCORD_CLIENT_ID"  # Replace with your bot's client ID
    permissions = 8  # Administrator permissions
    invite_link = f"https://discord.com/oauth2/authorize?client_id={client_id}&scope=bot&permissions={permissions}"
    return jsonify({'invite_link': invite_link})

# Serve favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

if __name__ == '__main__':
    app.run(debug=True)
