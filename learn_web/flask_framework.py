from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home!</h1>'

@app.route('/signin',methods=['GET'])
def signin_get():
    return '''  <form action=''/signin'' method=''post''>
                <p><input name=''username''></p>
                <p><input name=''password'' type=''password''></p>
                <p><button type=''submit''>Sign In<button></p>
                </form>'''


@app.route('/signin',methods=['POST'])
def signin_post():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello,admin!</h3>'
    else:
        return '<h3>Wrong username or password</h3>'

if __name__=='__main__':
    app.run()

#在命令端运行   python learn_flask_framework.py
# *Running on http://127.0.0.1:5000/
#在浏览器输入http://localhost:5000/         http://localhost:5000/sigin
#Flask自带的Server在端口5000上监听
#ctrl+c结束




























