from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from database import init_db

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure key


@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Redirect to login if not logged in

    with sqlite3.connect("expense_tracker.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT date, category, description, amount FROM expenses WHERE user_id = ? ORDER BY date DESC",
                       (session['user_id'],))
        expenses = cursor.fetchall()

    return render_template('index.html', expenses=expenses, username=session.get('username'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        with sqlite3.connect("expense_tracker.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
            user = cursor.fetchone()

        if user and check_password_hash(user[3], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password', 'danger')
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_hash = generate_password_hash(password)

        try:
            with sqlite3.connect("expense_tracker.db") as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                               (username, email, password_hash))
                conn.commit()
            flash('Account created successfully! You can now log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username or email already exists.', 'danger')
    return render_template('signup.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))


@app.route('/add_expense', methods=['POST'])
def add_expense():
    if 'user_id' not in session:
        flash("Please log in first!", "danger")
        return redirect(url_for('login'))

    date = request.form['date']
    category = request.form['category']
    description = request.form['description']
    amount = request.form['amount']

    with sqlite3.connect("expense_tracker.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (date, category, description, amount, user_id) VALUES (?, ?, ?, ?, ?)",
                       (date, category, description, amount, session['user_id']))
        conn.commit()

    flash("Expense added successfully!", "success")
    return redirect(url_for('home'))


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
