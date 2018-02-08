import pyautogui as pg
import time
import webbrowser

points = 0

# Question

answer = pg.prompt(
"""
Which would you rather do?

a) Help Eleven escape
b) Find Will Byers
c) Or talk to people in the upisde down world using christmas lights



"""


    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
    
# Question

answer = pg.prompt(
"""
What would you do if you found a random girl in the woods?

a) Offer Shelter
b) Think she's a weirdo
c) Think she's a weirdo until you discover she has super powers



"""


    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3



# Question

answer = pg.prompt(
"""
If you just escaped from "bad people" where would you run off too?

a) A restuarant
b) The woods
c) Keep running and never stop



"""


    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3



# Question

answer = pg.prompt(
"""
"Your son has just gotten kidnapped, what do you do?"

a) Go to the police
b) Freak out and buy some lights
c) Cry a few days and then go to the police



"""


    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


# Question

answer = pg.prompt(
"""
"You have just discovered your friend has been murdered. Do you care?"

a) Is that even a question??
b) Yay! Murder Party!!!!
c) Of course



"""


    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


# Question

answer = pg.prompt(
"""
"You have just discovered the upside down world. What do you do?"

a) Let the scientists experiment it
b) Go in an almost get killed by the monster
c) Mess with people in the real world



"""


    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3






# End of survey

#Mike
if points < 10:
    pg.alert("You are Mike")
    webbrowser.open("https://vignette.wikia.nocookie.net/strangerthings8338/images/4/48/Mike_Wheeler_S1.png/revision/latest?cb=20171025205131")

#Will's Mom
elif points < 14:
     pg.alert("You are Will's Mom")
    webbrowser.open("https://parade.com/wp-content/uploads/2016/08/winonaryder_strangerthings_netflix.jpg")
#Dustin
elif points < 19:
     pg.alert("You are Dustin")
    webbrowser.open("https://fsmedia.imgix.net/e0/b8/dd/55/2504/4748/a9d9/4a8c52e827d7/dustin-played-by-gaten-matarazzo-in-stranger-things.png")



















    


