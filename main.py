
import board
import time
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

btn = DigitalInOut(board.GP21)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

keyboard = Keyboard(usb_hid.devices)

while True:
    if not btn.value:
        keyboard.press(Keycode.CONTROL,Keycode.ALT,Keycode.T)
        time.sleep(0.05)
        keyboard.release_all()
        time.sleep(0.2)
