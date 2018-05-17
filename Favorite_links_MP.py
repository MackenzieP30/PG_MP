import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/watch?v=zjPwjNLETPA","https://www.youtube.com/watch?v=3q7oJuyy5Ac"]

music = ["https://www.spotify.com/us/premium/?utm_source=us-en_brand_contextual_text&utm_medium=paidsearch&utm_campaign=alwayson_ucanz_us_performancemarketing_core_brand+contextual+text+exact+us-en+google&gclid=CJHi5KuFutkCFQSMswod9HMAEw&gclsrc=ds","https://www.pandora.com/"]

answer = pg.prompt(
"""
Which would you rather do?
a) Watch videos
b) Listen to Music

"""
    )

if answer == "a":
    for i in videos:
        webbrowser.open(i)

elif answer == "b":
    for i in music:
        webbrowser.open(i)
