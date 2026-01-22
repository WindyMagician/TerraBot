import time
import pydirectinput
import pygetwindow as gw

# Focus Terraria
windows = gw.getWindowsWithTitle("Terraria")
assert windows, "Terraria window not found"
win = windows[0]
win.activate()
time.sleep(0.2)

# Test movement
pydirectinput.keyDown('d')   # move right
time.sleep(0.5)
pydirectinput.keyUp('d')

time.sleep(0.5)

pydirectinput.press('space')  # jump
