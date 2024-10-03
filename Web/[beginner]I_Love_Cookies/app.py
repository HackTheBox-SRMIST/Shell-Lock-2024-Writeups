from flask import Flask, render_template, request, redirect, url_for, make_response
import base64

app = Flask(__name__)

FLAG = "HTB{AdM1N_4c3s$_GraNt3d}"

USERNAME = "John"
PASSWORD = "john123"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == USERNAME and password == PASSWORD:
        encoded_username = base64.b64encode(username.encode()).decode()
        resp = make_response(redirect(url_for('dashboard')))
        resp.set_cookie('auth', encoded_username)
        return resp
    else:
        return "Invalid credentials! Try again."

@app.route('/dashboard')
def dashboard():
    auth_cookie = request.cookies.get('auth')
    if auth_cookie:
        decoded_username = base64.b64decode(auth_cookie).decode()
        
        if decoded_username == 'admin':
            return f"Welcome, admin! Here is your flag: {FLAG}"
        return render_template('dashboard.html', username=decoded_username)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
