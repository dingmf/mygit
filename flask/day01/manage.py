from flask import Flask, current_app, g, request, session

#创建APP实例
app = Flask(__name__)

#将路由和视图绑定
@app.route('/')
def index():
    print(current_app)
    g.string = '你好呀'
    print(request)
    print(session)
    return 'Hello Flask'

@app.route('/g/')
def get_g():
    # int('sasd')
    return g.string

#钩子函数 before_first_request
@app.before_first_request
def bf_first_request():
    #设置g
    g.string = 'before first request'

#before_request每次请求之前
@app.before_first_request
def bf_request():
    g.string = 'before request'


# after_request 每次请求之后，需要有一个参数，代表响应
@app.after_request
def af_request(param):
    param.set_cookie('username', 'lisi')
    return param

#teardown_request 每次请求之后执行，不管是否异常
@app.teardown_request
def td_request(exception=None):
    print('始终都会执行')


#url给视图函数传参
@app.route('/day01/<username>/')
def hello(username):
    return 'hello %s!' % (username,)

#传一个int型参数
@app.route('/user/<int:uid>/')
def get_user(uid):
    print(type(uid))
    return '# User %d' % (uid,)

#传一个浮点数
@app.route('/price/<float:price_tag>/')
def get_price(price_tag):
    print(type(price_tag))
    return 'the price of product is %f' % (price_tag,)


#传一个路径
@app.route('/path/<path:path>/')
def get_path(path):
    print(type(path))
    return 'the Path is %s' % (path,)

@app.route('/any/<any(a,b,c):abc>/')
def get_abc(abc):
    return '%s is passed' % (abc, )


if __name__ == '__main__':
    app.run(threaded=True)