from flask import render_template
from salesapp import app

# Định nghĩa các route
@app.route('/')
def home():
    return render_template('index.html')

# Chạy app
if __name__ == '__main__':
    app.run(debug=True)