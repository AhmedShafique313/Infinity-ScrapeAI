from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Login'
    else:
        return 'Login Form'

@app.route('/ScrapeAI')
def hello():
    return 'This is the Infinity ScrapeAI app page'

if __name__ == '__main__':
    app.run()