'''
django: 大而全重量级
flask: 轻量级
tornado：高并发
'''
# 1、导入模块
from flask import Flask, render_template, request, session
# 2、实例化
app = Flask(__name__)
# 3、路由
@app.route('/hello/')
def hello_world():
    return 'hello'

@app.route('/')
def index():
    if 'username'  in session:
        return '用户已登录'
    return '没有登录'

@app.route('/login/', methods=['POST','GET'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == 'admin123':
        session['username'] = username
        return "登录成功"
    return render_template('login.html')
app.secret_key = 'dwadadoawofdafawdfawwa'

@app.route('/logout/')
def logout():
    session.pop('username')
    return '退出'

if __name__ == '__main__':
    app.run()
