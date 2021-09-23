
import board
import time
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

trm_btn = DigitalInOut(board.GP21)
trm_btn.direction = Direction.INPUT
trm_btn.pull = Pull.UP

ext_trm_btn = DigitalInOut(board.GP20)
ext_trm_btn.direction = Direction.INPUT
ext_trm_btn.pull = Pull.UP

keyboard = Keyboard(usb_hid.devices)

while True:
    if not trm_btn.value:
        keyboard.press(Keycode.CONTROL, Keycode.ALT, Keycode.T)
        time.sleep(0.05)
        keyboard.release_all()
        time.sleep(0.2)

    if not ext_trm_btn.value:
        keyboard.press(Keycode.E, Keycode.X, Keycode.I, Keycode.T ,Keycode.ENTER)
        time.sleep(0.05)
        keyboard.release_all()
        time.sleep(0.2)