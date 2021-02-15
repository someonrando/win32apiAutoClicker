#! pythonw
import win32api, win32con, keyboard, time
def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
while keyboard.is_pressed('q') == False:
    click()
