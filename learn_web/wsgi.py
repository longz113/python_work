''''
一个完整的 Web 应用包含了如下流程:

1.浏览器向服务器发送一个 request；
2.服务器接收并处理 request，然后生成一个 HTML 文件；
3.服务器向浏览器返回一个包含 HTML 源码的 response；
4.浏览器接收 HTML 并将其显示出来。

WSGI接口是用来干什么的呢? 它是用来接收并处理 request 的！
一个基本的 WSGI 接口需要传入两个参数:
一个包含 request 信息的字典；一个返回 response 的方法。
这两个方法需要由 Web 服务器提供，
即由服务器调用 WSGI 接口从而实现完整 Web 应用的流程。
(使用WSGI接口去做服务器的工作)

使用WSGI顺序：
1.编写WSGI处理函数(请求信息的dict，响应函数)
2.启动WSGI
'''

def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    body='<h1>Hello, %s!</h1>' %(environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

from wsgiref.simple_server import make_server
# 创建一个服务器，IP地址为空，端口是8000，
#处理函数是application:
httpd=make_server('',8000,application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
#然后在命令行输入 python learn_wsgi.py 来启动WSGI
#启动成功后在浏览器输入 http://localhost:8000/
#在命令端按ctrl+c终止







































