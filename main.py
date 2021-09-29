
import board
import time
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

btn1 = DigitalInOut(board.GP2)
btn1.direction = Direction.INPUT
btn1.pull = Pull.UP

btn2 = DigitalInOut(board.GP3)
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP

btn3 = DigitalInOut(board.GP4)
btn3.direction = Direction.INPUT
btn3.pull = Pull.UP

btn4 = DigitalInOut(board.GP5)
btn4.direction = Direction.INPUT
btn4.pull = Pull.UP

btn5 = DigitalInOut(board.GP6)
btn5.direction = Direction.INPUT
btn5.pull = Pull.UP

btn6 = DigitalInOut(board.GP7)
btn6.direction = Direction.INPUT
btn6.pull = Pull.UP

btn7 = DigitalInOut(board.GP8)
btn7.direction = Direction.INPUT
btn7.pull = Pull.UP

btn8 = DigitalInOut(board.GP9)
btn8.direction = Direction.INPUT
btn8.pull = Pull.UP

keyboard = Keyboard(usb_hid.devices)

while True:
    if not btn1.value:
        keyboard.press(Keycode.CONTROL,Keycode.C)
        time.sleep(0.05)
        keyboard.release_all()
        time.sleep(0.5)

    if not btn2.value:
        keyboard.press(Keycode.CONTROL, Keycode.V)
        time.sleep(0.05)
        keyboard.release_all()
        time.sleep(0.5)

    if not btn3.value:
        keyboard.press(Keycode.CONTROL, Keycode.ALT, Keycode.T)
        time.sleep(0.05)
        keyboard.release_all()
        time.sleep(0.5)

    if not btn4.value:
        keyboard.press(Keycode.E, Keycode.X, Keycode.I,Keycode.T,Keycode.ENTER)
        time.sleep(0.05)
        keyboard.release_all()
        time.sleep(0.5)

    if not btn5.value:
        keyboard.press(Keycode.CONTROL, Keycode.S)
        time.sleep(0.05)
        keyboard.release_all()
        time.sleep(0.5)

    if not btn6.value:
        keyboard.press(Keycode.CONTROL, Keycode.ALT, Keycode.T)
        time.sleep(0.05)
        keyboard.release_all()
        time.sleep(0.5)

    if not btn7.value:
        keyboard.press(Keycode.CONTROL, Keycode.ALT, Keycode.T)
        time.sleep(0.05)
        keyboard.release_all()
        time.sleep(0.5)

    if not btn8.value:
        keyboard.press(Keycode.CONTROL, Keycode.ALT, Keycode.T)
        time.sleep(0.05)
        keyboard.release_all()
        time.sleep(0.5)
