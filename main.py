from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello flask'

@app.route('/about')
def about():
    return 'about page'

@app.route('/contact')
def contact():
    return 'contact page'

if __name__ == '__main__':
    app.run(debug=True)