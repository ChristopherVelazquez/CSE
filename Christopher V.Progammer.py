class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age, job, pay, position):
        super(Employee, self).__init__(name, age)
        self.job = job
        self.pay = pay
        self.position = position

    def  pay(self):
        print("You are paid %s amount." % self.pay)


class Progammer(Employee):
    def __init__(self, name, age, job, pay, position, intelligence, experience):
        super(Progammer, self).__init__(name, age, job, pay, position)
        self.intelligence = intelligence
        self.experience = experience

    def experience(self):
        print("You have this much %s" % self.experience)