name = "Mackenzie"

subjects = ["English", "Math", "History", "Science", "Spanish"]

print("Hello " + name)

print(subjects)

for i in subjects:
    print("One of my favorite classes is " + i)

homework = [" Being sooo productive right now -_-", " Doing one math problem and 'can't' do it", " Being so distractive you're a disease", " 'pro' procrastinator"]

for i in homework:
    print("You are actually " + i)


movies = []

while True:
    print("What movie do you like? Type 'end' to quit.")
    answer = input()

    if answer == "end":
        break
    else:
        movies.append(answer)

for i in movies:
    print("One of your favorite movies is " + i)
