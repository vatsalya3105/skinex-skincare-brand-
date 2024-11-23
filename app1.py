from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def create_connection():
    con = sqlite3.connect("users.db")
    return con

def create_table():
    con = create_connection()
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS newuser(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT,
            email TEXT, 
            username TEXT, 
            password TEXT
        )
    """)
    con.commit()
    con.close()
    return redirect("/feedback")

@app.route("/admin")
def admin():
    data = [
        {"id": 1, "name": "Vasu", "number": "1234567890"},
        {"id": 2, "name": "sweety", "number": "9871243210"},
        {"id": 3, "name": "amrutha", "number": "6178325126"},
    ]
    print(data)
    return render_template('admin.html', users=data)

@app.route("/")
def home():
    return render_template("webpage.html")

@app.route("/registration", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Get data from form
        name = request.form.get('first name')
        name = request.form.get('last name')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        con= create_connection()
        cur= con.cursor()
        cur.execute('''INSERT INTO newuser(first name,last name, email, username, password) VALUES(?, ?, ?, ?)''', (name, email, username, password))
        con.commit()
        cur.close()
        # Print data for debugging
        print(f"Received data: {name}, {email}, {username}, {password}")
        return redirect("/login")  # Redirect to login after registration
    return render_template("registration.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        return redirect("/feedback")  
    return render_template("loginpage.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

if __name__ == "__main__":
    create_connection()
    create_table()  # Make sure the table is created
    app.run(debug=True)