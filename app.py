# app.py

from flask import Flask, render_template, redirect, url_for, session, flash
from discord_integration import get_server_info  # Import function from discord_integration.py

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure secret key

# Dummy data for demonstration
bot_status = 'Online'
server_count = 1000  # Replace with actual data from your bot

# Function to check if user is logged in (decorator)
def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            flash('Please log in first.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Index route
@app.route('/')
def index():
    return render_template('index.html', bot_status=bot_status, server_count=server_count)

# Server information route
@app.route('/server/<int:guild_id>')
@login_required
def server_info(guild_id):
    server_info = get_server_info(guild_id)
    if server_info:
        return render_template('server_info.html', server_info=server_info)
    else:
        return render_template('error.html', message='Server not found')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Implement your authentication logic here (e.g., check credentials)
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            flash('You are now logged in.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You are now logged out.', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
