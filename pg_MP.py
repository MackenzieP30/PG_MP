import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',.3)

pg.hotkey('winleft','up')
pg.typewrite('espn.com\n',.3)
time.sleep(2)
pg.hotkey("ctrl" , "t")
pg.typewrite('haha just kidding',.3)
pg.hotkey('winleft','d')
pg.hotkey('alt','f4')

time.sleep(0.5)
pg.hotkey('up')
pg.hotkey('enter')
