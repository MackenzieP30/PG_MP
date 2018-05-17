print("What's your name?")
name = input()

if name == "Mackenzie":
    print("Welcome Back")
else:
    print("Hello " + name)


print("What's your favorite sport?")
sport = input()

if sport == "Softball":
    print("That's my favorite too!")
elif sport == "Basketball":
    print("I love playing Basketball too.")
elif sport == "soccer":
    print("Meh, I'm not good at Soccer.")
else:
    print(sport + " is fun")

print("What's your favorite TV show?")
tvshow = input()

if tvshow == "Glee":
    print("That's my favorite. Who's your favorite character?")
    character = input()
    if character == "Finn":
        print("He's my absolute favorite as well!")

print("Where are you from?")
country = input()

if country == "America":
    print("Cool! Me too! What state?")
    state = input()
    if state == "Connecticut":
        print("Wow! Me too!")
    else:
        print("That's a cool state.")
else:
    print("That's so cool!")



