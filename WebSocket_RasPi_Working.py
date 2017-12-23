import sys
sys.path.insert(0, '~/AutomationProjects/lightSwticher.py')
from ws4py.client.threadedclient import WebSocketClient
import json
import lightSwticher
import  string
import RepeatTimer

class DummyClient(WebSocketClient):

    theBoy = SomeShit()
    starttime = time.time()

    def opened(self):
        print 'Connection Opened'
        theValue = {}
        theValue["senderID"] = "raspberryPi"
        theValue["toID"] = "60238C56-A571-4107-B0C9-68DDBDF67055"
        theValue["message"] = "Pi Talking : Back Super man."
        json_data = json.dumps(theValue)
        self.send(json_data)
        self.theBoy.lightCheck()
        rt = RepeatedTimer(20, self.keepAlive, "World")  # it auto-starts, no need of rt.start()

    def keepAlive(self, message):
        print "tick"
        self.ping('Straying ALive Man')

    def closed(self, code, reason=None):
        print "Closed down", code, reason
        if code == 1006:
            self.setupConnection

            # self.theBoy.cleanUp()

    def received_message(self, m):
        print 'We Got a Message' + str(m)
        # theBoy = SomeShit()
        self.theBoy.processMessage(m)

    def unhandled_error(self, error):
        print "Unhanldled Error" + error

    def setupConnection(self):
        ws.connect()
        ws.run_forever()

    if __name__ == '__main__':
        try:
            # ws = DummyClient('ws://0.0.0.0:9090/doSomeShit', protocols=['http-only', 'chat'])
            ws = DummyClient('ws://gentle-island-29960.herokuapp.com/doSomeShit', protocols=['http-only', 'chat'])
            ws.setupConnection()
        except KeyboardInterrupt:
            ws.close()