# import random  # This should be on line 1
# # This is working
# print ("Hello World")
#
# #Christopher Velazquez
# #(This is Python 2.7)
#
# print (3 + 5)
# print (5 - 3)
# print (3 * 5)
# print (6 / 2)
# print (3**2)
#
# print # this makes a new line. In python 3.6, it looks like:print ()
# print ("See if you can figure this out")
# print(13 % 12)
#
# car_name= "oof"
# car_type= "Lamborgnini Sesto  Elemento"
# car_cylinders = 8
# car_mpg = 9000.1
#
#Inling printing
# print ("I have a car called %s" % car_name)
# print ("I have a car called %s. It's a %s," % (car_name, car_type))
#
# #Asking for input
# name = raw_input("What is your name ?")#In python 3 it is just called input
# print("Hello %s, "% name)

#funtions

# def print_hw():
#     print("Hello World")
#
# print_hw()
# print_hw()
# print_hw()
#
# def say_hi(name) :
#     print("Hello %s" % name)
#
#
#
#     print("Enjoy your day.")
#
# say_hi("John")
#
# def print_age(name, age):
#     print ("%s is %d years old." %  (name,age))
#     age += 1  #age = age + 1
#     print("Next year, they will be %d" % age)
#
# print_age ("John", 15)
#
# def f (x) :
#     return x**3 + 4 * x**2 + 7 * x - 4
#
# print(f(3))
# print(f(4))
# print(f(5))
# # If statements
#
#
# def grade_calc(percentage):
#     if percentage >=90:
#         return "A"
#     elif percentage < 90 and percentage >= 90 :
#         return "B"
#     elif percentage >= 70 :
#         return "C"
#
#     '''Write a function called "happy_bday" that "sings" (prints) Happy birthday
#
# It must take one parameter called "name"
# '''
#
# def happy_bday(name):
#     print("Happy birthday to you" + ",")
#     print("Happy birthday to you" + ",")
#     print("Happy birthday to " + name + ",")
#     print("Happy birthday to you" + ",")
# happy_bday("John")
#
#
# #loops
# for num in range(100000000000000):
#      print(num+1)
#
# a = 1
# while a <= 10:
#     print(a)
#     a+=1
#
# # Random Numbers
#
# print(random.randint(0, 100))
# """

# # Lists
# the_count = [1, 2, 3, 4, 5]
# shopping_list = ["Noodles", "Eggrolls", "Milk", "Rice", "Chips"]
# print(shopping_list[2])
#
# print(len(shopping_list))
#
# # Going through a list
# for item in shopping_list:
#     print(item)
# for num in the_count:
#     print(num * 2)
# len(shopping_list)      # Gives me the lenth of the list
# range(3)   # Gives me the list of the numbers 0 through 2
# range(len(shopping_list))  # A list of every index
#
# for num in range(len(shopping_list)):
#     item = shopping_list[num]
#     print("The item at index %d is %s" %(num, item))
#
# # Turn things into a list
# str1 = "Ello Class Open bob and vagene"
# listOne = list(str1)
# print(listOne)
# listOne[11] = '.'
# print(listOne)
# print("".join(listOne))
#
# # Add things to a list
# shopping_list.append("cereal")
# print(shopping_list)
#
# # Removing things from a list
# shopping_list.remove("soda")
# print(shopping_list)
# shopping_list.pop(0)
# print(shopping_list)
#
# # the string class
# import string
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.punctuation)
# print(string.digits)
#
# # Dealing with strings
# strTwo="ThIs iS a VeRY oDd sEnTENce"
# lowercase = strTwo.lower()
# print(lowercase)


# Dictionaries - Made up of Key: Value pairs
dictionary = {'name': 'Lance', 'age': 23, 'height': 5 * 12 + 7}

# Accessing dictionaries
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])

# adding to a dictionary
dictionary['weight'] = 280
print(dictionary)

large_dictionary = {
    'CA': 'California',
    'FL': 'Florida',
    'OH': 'Ohio'
}
print(large_dictionary['FL'])
larger_dictionary = {
    'CA': [
        'Fresno',
        'Sacremento',
        'Los Angeles'
    ],
    'FL': [
        'Tampa',
        'Orlando',
        'Miami'
    ],
    'OH': [
        'Cleverland',
        'Cincinnati',
    ]
}
print(larger_dictionary['FL'])
print(larger_dictionary['FL'][2])
print(larger_dictionary['OH'][1])

largest_dictionary = {
    'CA': {
        'NAME': 'California',
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Nevada',
            'Arizona'
        ]
    },
    'AZ': {
        'NAME': 'Arizona',
        'POPULATION': 6931000,
        'BORDER ST': [
            'California',
            'Utah',
            'Nevada',
            'New Mexico'
        ]
    },
    'NY': {
        'NAME': "New York",
        'POPULATION': 19750000,
        'BORDER ST': [
            'Vermont',
            'Massachusetts',
            'Connecticut',
            'Pennsylvania',
            'New Jersey'
        ]
    }
}
current_nods = largest_dictionary['NY']
print(current_nods['NAME'])
print(current_nods['POPULATION'])


