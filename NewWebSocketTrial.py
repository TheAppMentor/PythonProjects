
#!/usr/bin/python
import websocket
import thread
import time

from websocket import create_connection, WebSocket

class MyWebSocket(WebSocket):
    def recv_frame(self):
        frame = super().recv_frame()
        print('yay! I got this frame: ', frame)
        return frame

    def on_message(self):
        print "We Got a Message man"

def on_message(self):
    print "We Got a Message man"

def on_error(self):
    print "We Got a Error man"

def on_close(self):
    print "We Got a Close"

def on_open(self):
    print "We Got a Open"

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = create_connection('ws://gentle-island-29960.herokuapp.com/doSomeShit')

    ws = websocket.WebSocket("ws://gentle-island-29960.herokuapp.com/doSomeShit",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    # ws.connect("ws://gentle-island-29960.herokuapp.com/doSomeShit")
    ws.on_open = on_open
    # MyWebSocket().connect("ws://gentle-island-29960.herokuapp.com/doSomeShit")

    #ws.run_forever()