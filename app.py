from flask import Flask, request, render_template, jsonify, redirect, url_for

app = Flask(__name__)

users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        users.append({'username': username, 'email': email, 'password': password})
        return jsonify({'message': '用户注册成功', 'redirect': url_for('index')})
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        user = next((u for u in users if u['email'] == email and u['password'] == password), None)
        if user:
            return jsonify({'message': '登录成功', 'redirect': url_for('detection')})
        else:
            return jsonify({'message': '登录失败'}), 401
    return render_template('login.html')

@app.route('/detection')
def detection():
    return render_template('detection.html')

if __name__ == '__main__':
    app.run(debug=True)
