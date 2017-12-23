from ws4py.client.threadedclient import WebSocketClient
import json

class SomeShit():

    def hello(self):
        print('Function talking.')

    def processMessage(self, message):
        print('I am simply talking man')
        print 'testBoy'.upper()
        if (str(message)).upper() == "ON":
            print 'Bloody On man'
        print(message)
        return
        # return 'super message man'
        #ws = MyClient('ws://0.0.0.0:9090/doSomeShit', protocols=['http-only', 'chat'])

class DummyClient(WebSocketClient):
    def opened(self):

        theValue = {}
        theValue["senderID"]    =  "raspberryPi"
        theValue["toID"]        =  "60238C56-A571-4107-B0C9-68DDBDF67055"
        theValue["message"]     =  "Pi Talking : Back Super man."
        json_data = json.dumps(theValue)
        self.send(json_data)

    def closed(self, code, reason=None):
        print "Closed down", code, reason

    def received_message(self, m):
        print('Received Message from Server')
        print(m)
        theBoy = SomeShit()
        theBoy.processMessage(m)

    def unhandled_error(self, error):
        print "Unhanldled Error" +  error


if __name__ == '__main__':
    try:
        #ws = DummyClient('ws://0.0.0.0:9090/doSomeShit', protocols=['http-only', 'chat'])
        ws = DummyClient('ws://gentle-island-29960.herokuapp.com/doSomeShit', protocols=['http-only', 'chat'],heartbeat_freq=0.1)
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()
