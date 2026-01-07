# import các class từ thư viện flask
from flask import Flask, render_template

# Khởi tạo app Flask từ file hiện tại
app = Flask(__name__)

# Tạo một list post
posts = [
    {
        'author': 'Alex Ferguson',
        'title': 'My First Post',
        'subtitle': 'My subtitle 1',
        'description': 'My description 1',
        'content': 'My content 1',
        'datePublished': '18-08-2022',
    },
    {
        'author': 'Oscar Bobb',
        'title': 'My Second Post',
        'subtitle': 'My subtitle 2',
        'description': 'My description 2',
        'content': 'My content 2',
        'datePublished': '20-09-2023',
    }
]

# Viết các route cho app
@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/user/<username>')
def profile(username):
    return f'Welcome {username}!'

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

# Chạy ứng dụng Flask
if __name__ == '__main__':
    app.run(debug=True)