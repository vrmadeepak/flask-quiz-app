from flask import Flask, render_template, request
import MySQLdb

app = Flask(__name__)

def mydb():
    global c, conn
    conn = MySQLdb.connect(
        host="sql6.freemysqlhosting.net",
        port=3306,
        user="sql6424443",
        password="YYBPDNQbM3",
        database="sql6424443"
    )
    c = conn.cursor()


@app.route('/')
def index():
    mydb()
    print(conn)
    return render_template('index.html', form = [['name', 'Enter Name', 'text', 'Enter your username'], ['password', 'Enter password', 'password', 'Enter your password']])

@app.route('/login', methods=['POST'])
def login():
    req = request.form
    print(req)
    return 'Submitted'

@app.route('/signup', methods=['POST'])
def signup():
    req = request.form
    return 'User Signed Up'

if(__name__=='__main__'):
    app.run() 