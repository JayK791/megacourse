# import datetime
# mynow = datetime.datetime.now()
# print(mynow)

# monday_temperatures = [9.1, 8.8, 7.5]
# student_grades = {"Marry" : 9.1, "Sim" : 8.8, "John": 7.5}

# mysum = sum(student_grades.values())
# length=len(student_grades)
# mean = mysum/length
# print(mean)


# monday_temperatures = (1, 4, 5) -> can't use monday_temperatures.append(7)
# monday_temperatures = [1, 4, 5] -> able

# monday_temperatures.index(8.8, 2) -> find 8.8 from 2
#  monday_temperatures[1:4] -> find values  from 1 to 3
#  monday_temperatures[1:] -> find values  from 1 
#  monday_temperatures[-1:] -> find values  from 1 from the end, but there's no 0
#  monday_temperatures = ["Hello", 3, 7]
#  monday_temperatures[0][2] => 'l' -> find values in 0 
# eng_port = {"rain": "chuba", "sun": "sol"}
#  eng_port["sun"] => 'sol'


def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else: 
        the_mean = sum(value) / len(value)
    return the_mean

student_grades = {"Marry" : 9.1, "Sim" : 8.8, "John": 7.5}

print(mean(student_grades))
 
def foo(password): 
        if len(password) > 8:
            return True
        else:
            return False

def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"
    
# user_input = input("Enter temperature:")
# print(weather_condition(user_input))
# ---> error -> user input will be converted to string

user_input = float(input("Enter temperature:"))
print(weather_condition(user_input))


# %s -> 
# user_input = input("Enter your name: ")
# message = "Hello %s!" % user_input => Hello user_input!
# message = f"Hello {user_input}"


# monday_temperatures = [9.1, 8.8, 7.6]

# for temperature in monday_temperatures:
#     print(round(temperature))

# for potato in "hello":
#     print(potato)


# username = ' '
# while username != 'pypy':
#     username = input("Enter your name: ")



# while True:
#     username = input("Enter username: ")
#     if username == "pypy":
#         break
#     else:
#         continue


# def sentence_maker(phrase):
#     interrogatives = ("how", "what", "why")
#     capitalized = phrase.capitalize()
#     if phrase.startwith(interrogatives):
#         return "{}?".format(capitalized)
#     else:
#         return "{}.".format(capitalized)
    
# results = []

# while True:
#     user_input = input("Say something: ")
#     if user_input == "\end":
#         break
#     else:
#         results.append(sentence_maker(user_input))

# print(" ".join(results))


# temps = [221, 234, 340, 230]

# new_temps = []
# for temp in temps:
#     new_temps.append(temp / 10)

# print(new_temps)


# new_temps = [temp / 10 for temp in temps]


# temps = [221, 234, -9999, 230]

# new_temps = [temp / 10 for temp in temps if temp != -9999]

# print(new_temps)


# new_temps = [temp / 10 if temp != - 9999 else 0 for temp in temps]




# def foo(lst):
#     return [i if not isinstance(i, str) else 0 for i in lst ]

def foo(lst):
    return [i if isinstance(i, int) else 0 for i in lst]

print(foo([99, 'no date', 95, 94, 'no date']))


def mean(*args):
    return sum(args) / len(args)


def mean(**kwargs):
    return kwargs

print(mean(a=1, b=2, c=3))

# keyward arguments -> eg. a=1, b=2 ... return dictionary

myfile = open("fruits.txt")
print(myfile.read()) #show content in fruits.txt

content = myfile.read()
print(content)
print(content) #this will print myfile twice

myfile.close() #close file -> you can't do actioin with myfile

with open("fruits.txt") as myfile:
    content = myfile.read() #no need to close file

with open("files/fruits.txt") as myfile:
    content = myfile.read() #when fruits.txt isn't in the same folder

with open("files/vegetables.txt", "w") as myfile:
    myfile.write("Tomato") #"w" -> write. create new file. if you apply it to exist file, it'll be overwritten
    myfile.write("Onion/nPotato/nCucumber")

with open("files/vegetables.txt", "x") as myfile:
    myfile.write("Tomato") #"x" -> create new file. exist file name  can't be used
    myfile.write("Onion/nPotato/nCucumber")

with open("files/vegetables.txt", "a") as myfile:
    myfile.write("Tomato") #"a" -> add items in the selected file. "a+" -> read and write 
    mtfile.seek(0) # move cursor to 0
    myfile.write("Onion/nPotato/nCucumber")

