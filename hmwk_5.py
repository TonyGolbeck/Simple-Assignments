# 3-1. Names:
names = ['Josh', 'Ricky', 'Kenny', 'Devin']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 3-2. Greetings:
print("It's great to see you,", names[0])

# 3-3. Your Own List:
trans = ['bike', 'car', 'plane']
print('I own a', trans[0])
print('I like driving a', trans[1])
print('I enjoy flying in a', trans[2])

# 3-4. Guest List:
guests = ['Morgan Freeman', 'Allan Watts', 'Gordon Ramsay']
print('You are invited to dinner! ', guests[0])
print('You are invited to dinner! ', guests[1])
print('You are invited to dinner! ', guests[2])

# 3-5. Changing Guest List:
cannot_makeit = 'Gordon Ramsay'
guests.remove(cannot_makeit)
print(cannot_makeit.title() + ' cannot make it')
guests.insert(0, 'Julia')
print('You are invited to dinner! ', guests[0])
print('You are invited to dinner! ', guests[1])
print('You are invited to dinner! ', guests[2])

# 3-6. More Guests:
print('We found a bigger dinner table!')
guests.insert(0, 'Josh')
guests.insert(2, 'Riki')
guests.append('Greg')
print('You are invited to dinner! ', guests[0])
print('You are invited to dinner! ', guests[1])
print('You are invited to dinner! ', guests[2])
print('You are invited to dinner! ', guests[3])
print('You are invited to dinner! ', guests[4])
print('You are invited to dinner! ', guests[5])

# 3-7. Shrinking Guest List:
print('Sorry we can only invite two people for dinner')
guests.pop(1)
print('Sorry Julia we cannot invite you to dinner')
guests.pop(1)
print('Sorry Riki we cannot invite you to dinner')
guests.pop(1)
print('Sorry Morgan we cannot invite you to dinner')
guests.pop(2)
print('Sorry Greg we cannot invite you to dinner')
print('You are still invited, ' + guests[0] + '!')
print('You are still invited, ' + guests[1] + '!')
del guests[0]
del guests[0]
print(guests)

# 3-8. Seeing the World
places = ['germany', 'iceland', 'japan', 'switzerland', 'ireland']
print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

# 3-9. Dinner Guests:
print(len(guests))
print('-----------------------------------------------------------')
#-----------------------------------------------------------------------

# 4-1. Pizzas:
pizzas = ["pepperoni", "sausage", "cheese", "chicken"]
print(pizzas)
for pizza in pizzas:
    print('I like ' + pizza + ' pizza')
print('Pepperoni pizza is great!')
print('sausage pizza is neat')
print('Cheese pizza is my favorite')
print('I really love pizza!')
print(pizzas)

# 4-2. Animals:
animals = ['dog', 'cat', 'fox']
for animals in animals:
    print('a ' + animals.title() + ' would make a great pet!')
print('All of these animals walk on four legs.')

# 4-3. Counting to twenty:
for value in range(1,21):
    print(value)

# 4-4. One Million:
million = list(range(1,1000001))
#for million in million:
  #  print(million)

# 4-5. Summing a million:
print(sum(million))

# 4-6. Odd Numbers:
odds = list(range(1,21,2))
for odds in odds:
    print(odds)

# 4-7. Threes:
threes = list(range(3,30,3))
for threes in threes:
    print(threes)

# 4-8. Cubes:
cubes = [value**3 for value in range(1,11)]
print(cubes)

# 4-9. Cube Comprehension:
cube = [value**3 for value in range(1,11)]

# 4-10. Slices:
ppl = ['frank', 'bill', 'jesse', 'josh', 'riki', 'morgan', 'john', 'jess', 'micheal']
print("The first three people on the list are:")
print(ppl[0:3])
print("The middle three people on the list are:")
print(ppl[3:6])
print("The last three people on the list are:")
print(ppl[6:9])


# 4-11. My Pizzas, Your Pizzas:
friend_pizzas = ['pepperoni', 'sausage', 'cheese', 'BBQ']
print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)
print("My friends favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)

# 4-13. Buffet:
buffet = ("chicken", "mac n cheese", "beef", "pasta", "perogi")
for food in buffet:
    print(food)

buffet = ("pork", "mac n cheese", "beef", "sushi", "perogi")
print('revised menu:')
for food in buffet:
    print(food)
print('----------------------------------------------------------')
#---------------------------------------------------------------------

# 5-1. Conditional Tests:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print("\nIs car == 'nissan'? I predict False.")
print(car == 'nissan')
print("\nIs car == 'bently'? I predict False.")
print(car == 'bently')
print("\nIs car == 'chevy'? I predict False.")
print(car == 'chevy')
print("\nIs car == 'lamborgini'? I predict False.")
print(car == 'lamborgini')
print("\nIs car == 'Subaru'? I predict True.")
print(car.title() == 'Subaru')
print("Is car != 'bently'? I predict True.")
print(car != 'bently')

# 5-2. More Conditional Tests:
bike = 'Trycicle'
print(bike == 'motorcyle')
print(bike.lower() == 'trycicle')
num = 20
print(num >= 5)
print(num <= 5)
print(num == 5)
print(num != 5)
banned_users = ['steve', 'hank', 'john']
'steve' in banned_users
'eric' not in banned_users

# 5-3. Alien Colors #1:
alien_color = 'green'
if alien_color == 'green':
    print("You've earned 5 points!")
alien_color2 = 'red'
if alien_color2 == 'green':
    print("You've earned 5 points!")

# 5-4. Alien Colors #2:
if alien_color2 == 'green':
    print("You've earned 5 points!")
else:
    print("You've earned 10 points!")
if alien_color == 'green':
    print("You've earned 5 points!")
else:
    print("You've earned 10 points!")

# 5-5. Alien Colors #3:
alien_color = 'yellow'
if alien_color == 'green':
    print("You've earned 5 points!")
elif alien_color == 'yellow':
    print("You've earned 10 points!")
else:
    print("You've earned 15 points!")

# 5-6. Stages of live:
age = 18
if age <= 2:
    print("You are a baby")
elif age <= 4:
    print("You are a toddler")
elif age <= 13:
    print("You are a kid")
elif age <= 20:
    print("You are a teenager")
elif age <= 65:
    print("You are an adult")
else:
    print("You are an elder")

# 5-7. Favorite fruit:
favorite_fruit = ['mango', 'dragon fruit', 'pear']
if 'mango' in favorite_fruit:
    print("I really like mangos!")
if 'dragon fruit' in favorite_fruit:
    print("I really like dragon fruit!")
if 'apple' in favorite_fruit:
    print("I really like apples!")
if 'pear' in favorite_fruit:
    print("I really like pears!")
if 'kiwi' in favorite_fruit:
    print("I really like kiwis!")

# 5-8. Hello admin:
usernames = ['admin', 'tobi', 'tia', 'diru', 'morioh']
for username in usernames:
    if username == 'admin':
        print("Hello Admin, would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again.")

# 5-9. No Users:
usernames = []

if username == 'admin':
    for username in usernames:
        print("Hello Admin, would you like to see a status report?")
else:
    print("We need to find some users!")

# 5-10. Checking usernames:
current_users = ['admin', 'tobi', 'tia', 'diru', 'morioh']
new_users = ['steve', 'alex', 'diru', 'bill', 'josh']
for user in new_users:
    if user in current_users:
        print("That username has already been taken")
    else:
        print("That username is available")

# 5-11. Ordinal Numbers:
number = list(range(1,10))
for i in number:
    if i == 1:
        print("1st")
    if i == 2:
        print("2nd")
    if i == 3:
        print("3rd")
    else:
        print(i)
