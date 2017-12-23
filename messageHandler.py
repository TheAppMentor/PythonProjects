import lightSwticher
import time

class SomeShit():

    switchBoy = lightSwticher.LightSwitcher()

    def hello(self):
        print('Function talking.')

    def processMessage(self, message):
        print(message)
        #switchBoy = lightSwticher.LightSwitcher()
        if str(message).upper() == 'ON':
            self.switchBoy.turnOn()
            return
        if str(message).upper() == 'OFF':
            self.switchBoy.turnOff()
            return

    def cleanUp(self):
        self.switchBoy.turnOff()
        self.switchBoy.cleanUp()

    def resetLight(self):
        switchBoy = lightSwticher.LightSwitcher()
        switchBoy.turnOff()

    def lightCheck(self):
        self.switchBoy.turnOn()
        time.sleep(1.0)
        self.switchBoy.turnOff()