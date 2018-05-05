from bottle import run, route, static_file

@route('/')
def index():
    return static_file('index.html', 'C:/myrepository/liujiayu_gai/')

@route('/resource/<filename>')
def staticFile(filename):
    return static_file(filename, 'C:/myrepository/liujiayu_gai/resource')    #改为文件夹绝对路径

run(host='192.168.1.104', port='8080')    #改为ipconfig查询的地址