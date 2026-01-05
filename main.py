# import các class từ thư viện flask
from flask import Flask, render_template

# Khởi tạo app Flask từ file hiện tại
app = Flask(__name__)

# Viết các route cho app
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Chạy ứng dụng Flask
if __name__ == '__main__':
    app.run(debug=True)