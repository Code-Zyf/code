from flask import Flask, render_template

app = Flask(__name__)

@app.route('/add/user')
def add_user():
    return render_template('nemone.html')

if __name__ == '__main__':
    app.run()


