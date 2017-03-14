__author__ = 'nrao'

class Person(object):

    def __init__(self, name, age):
        self.name = name
        # Private attribute
        self.__age = age

    def say_hello(self):
        print "%s aged %d says Hi!" % (self.name, self.__age)
        self.__get_age()

    def __del__(self):
        print "%s aged %d says bye!" % (self.name, self.__age)

    # Private method
    def __get_age(self):
        print "%s is aged %d" % (self.name, self.__age)

    @staticmethod
    def fart():
        print "broom..!!"

me = Person("naveen", 34)
me.say_hello()

print me.name

# IMPORTANT ACCESS METHOD
me._Person__get_age()
me.fart()



