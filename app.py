from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Login'
    else:
        return 'Login Form'

@app.route('/ScrapeAI')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()