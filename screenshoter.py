import pyscreenshot as ImageGrab
import time


def gogo():
    while True:
        im=ImageGrab.grab()
        filename = '{}_screenshot.png'.format(time.strftime("%Y%m%d-%H%M%S"))
        print '{}'.format(filename)
        im.save(filename)
        time.sleep(1)

if __name__ == '__main__':
	gogo()