import win32api
import win32con
import time
from bottle import request, Bottle, abort
from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler

app = Bottle()
@app.route('/websocket')
def handle_websocket():
    wsock = request.environ.get('wsgi.websocket')
    if not wsock:
        abort(400, 'Expected WebSocket request.')
    while True:
        try:
            message = wsock.receive()
            print(message)
            if message == 'rightward_start':
                win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(68, 0, 0, 0)
            elif message == 'rightward_end':
                time.sleep(0.1)
                win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif message == 'leftward_start':
                win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(65, 0, 0, 0)
            elif message == 'leftward_end':
                time.sleep(0.1)
                win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif message == 'upward_start':
                win32api.keybd_event(87, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(87, 0, 0, 0)
            elif message == 'upward_end':
                time.sleep(0.1)
                win32api.keybd_event(87, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif message == 'downward_start':
                win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(83, 0, 0, 0)
            elif message == 'downward_end':
                time.sleep(0.1)
                win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif message == 'softshoot':
                win32api.keybd_event(85, 0, 0, 0)
                time.sleep(0.1)
                win32api.keybd_event(85, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif message == 'heavyshoot':
                win32api.keybd_event(74, 0, 0, 0)
                time.sleep(0.1)
                win32api.keybd_event(74, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif message == 'softfoot':
                win32api.keybd_event(73, 0, 0, 0)
                time.sleep(0.1)
                win32api.keybd_event(73, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif message == 'heavyfoot':
                win32api.keybd_event(75, 0, 0, 0)
                time.sleep(0.1)
                win32api.keybd_event(75, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif message == 'speone':
                win32api.keybd_event(83, 0, 0, 0)
                time.sleep(0.1)
                win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(68, 0, 0, 0)
                time.sleep(0.1)
                win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(85, 0, 0, 0)
                time.sleep(0.1)
                win32api.keybd_event(85, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif message == 'spetwo':
                win32api.keybd_event(83, 0, 0, 0)
                time.sleep(0.1)
                win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(65, 0, 0, 0)
                time.sleep(0.1)
                win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(85, 0, 0, 0)
                time.sleep(0.1)
                win32api.keybd_event(85, 0, win32con.KEYEVENTF_KEYUP, 0)
            else:
                wsock.send(message)
            wsock.send('reset')
        except WebSocketError:
            break

server = WSGIServer(("192.168.1.104", 8081), app, handler_class=WebSocketHandler)
#server = WSGIServer(("10.162.106.171", 8081), app, handler_class=WebSocketHandler)       #改为ipconfig查询的地址
server.serve_forever()
