import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',.5)
time.sleep(.5)
pg.hotkey('winleft','up')

pg.typewrite('youtube\n',.2)
time.sleep(1)
