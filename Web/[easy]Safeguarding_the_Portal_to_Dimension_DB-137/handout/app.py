from flask import Flask, render_template, request, redirect, url_for, session, g
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key'  

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db()
        
        
        cursor = conn.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
        user = cursor.fetchone()

        if user:
            session['user_id'] = user[0]  
            session['username'] = user[1]  
            return redirect(url_for('user_dashboard'))
        else:
            return "<body style='background-color: black; color: white'>Invalid login.<br>(BURPP...) Looks like I need to inject. <br><img src='/static/images/rickinject.jpg' height='300' width='500' style='border-radius: 50px;'></body>"
    
    return render_template('login.html')


@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db()

        
        cursor = conn.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
        admin = cursor.fetchone()

        if admin and admin[1] == 'admin':
            session['admin'] = admin[1]
            return redirect(url_for('admin_dashboard'))
        else:
            return "Invalid admin login."

    return render_template('admin_login.html')


@app.route('/dashboard')
def user_dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return f"<body style='background-color: black; color: white'><h1 style='font-size: 50px; font-family: Tahoma'>Welcome, {session['username']}!</h1><br><a href='/logout' style='font-family: Tahoma'>Logout</a><br><a href='/user?id={session['user_id']}' style='font-family: Tahoma'>Your Profile</a></body>"


@app.route('/user')
def profile():
    user_id = request.args.get('id')  
    if not user_id:
        return "User ID is required."

    conn = get_db()
    
    # Fetch user by ID (this is where IDOR vulnerability occurs)
    cursor = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    if user[1] == 'admin':
        return "<body style='background-color: black; color: white'>Access denied.<br><img src='/static/images/ricklol.gif' style='border-radius: 50px;'></body>"

    if not user:
        return "User not found."

    # Prevent access to the admin profile through IDOR
    

    return f"<body style='background-color: black; color: white'>Profile of {user[1]}<br>Email: {user[2]}<br>{user[4]}<br><a href='/dashboard'>Back to Dashboard</a></body>"

# Admin dashboard after login
@app.route('/admin_dashboard')
def admin_dashboard():
    if 'admin' not in session:
        return redirect(url_for('admin_login'))
    return render_template('admin_dashh.html')
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/')
def index():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
