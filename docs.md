## 1. Setting & run Flask
```
    Những cái cần nắm:
    - pip install flask
    - route() ko tham số
    @app.route('/   ')
    def home():
        return "Hello Flask"
    - route() có tham số
    @app.route('/user/<name>')
    def user(name):
        return f"Hello {name}"
    - Chạy flask:
    if __name__ == '__main__'
        app.run(debug=True)
```

## 2. Templates:
```
    jinja2:
    - render_template() & truyền data sang HTML
    return render_template('home.html', name='Thủy')
    <h1>Xin chào {{ name }}</h1>
    - {% %}: dùng để viết logic (như: ifelse, loop, block, extends)
    - {{ }}: dùng để hiển thị data
```