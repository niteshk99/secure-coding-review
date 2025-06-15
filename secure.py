from flask import Flask, request
import sqlite3
import bcrypt

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password'].encode('utf-8')

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result and bcrypt.checkpw(password, result[0]):
        return "Login successful"
    else:
        return "Invalid credentials"

if __name__ == '__main__':
    app.run(debug=False)
