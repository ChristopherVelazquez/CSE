import random  # This should be on line 1
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
# # Inling printing
# print ("I have a car called %s" % car_name)
# print ("I have a car called %s. It's a %s," % (car_name, car_type))
#
# #Asking for input
# name = raw_input("What is your name ?")#In python 3 it is just called input
# print("Hello %s, "% name)

#funtions

def print_hw():
    print("Hello World")

print_hw()
print_hw()
print_hw()

def say_hi(name) :
    print("Hello %s" % name)



    print("Enjoy your day.")

say_hi("John")

def print_age(name, age):
    print ("%s is %d years old." %  (name,age))
    age += 1  #age = age + 1
    print("Next year, they will be %d" % age)

print_age ("John", 15)

def f (x) :
    return x**3 + 4 * x**2 + 7 * x - 4

print(f(3))
print(f(4))
print(f(5))
# If statements


def grade_calc(percentage):
    if percentage >=90:
        return "A"
    elif percentage < 90 and percentage >= 90 :
        return "B"
    elif percentage >= 70 :
        return "C"

    '''Write a function called "happy_bday" that "sings" (prints) Happy birthday
    
It must take one parameter called "name"
'''

def happy_bday(name):
    print("Happy birthday to you" + ",")
    print("Happy birthday to you" + ",")
    print("Happy birthday to " + name + ",")
    print("Happy birthday to you" + ",")
happy_bday("John")


#loops
for num in range(100000000000000):
     print(num+1)

a = 1
while a <= 10:
    print(a)
    a+=1

# Random Numbers

print(random.randint(0, 100))


