
class LightSwitcher():
    def turn_on(self, gpio_num):
        print 'We will now turn on' + gpio_num

    def turn_off(self, gpio_num):
        print 'We will now turn off' + gpio_num

    def clean_up(self):
        print 'We will clean up all GPIO Pins'