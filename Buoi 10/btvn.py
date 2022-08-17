# Exercise 8.1
# 1.What is the difference between a local variable and an object’s attribute?
# Local variable is used inside function, whereas object’s attribute can be used thorough Class, first defined

# 2. What method is called when the object is created?
# __init__(self,...)

# 3. Write the line of code you would use to call the do something method of and object instance obj. Assume
# that the do something method for obj exists.
# obj.do_something()


# Exercise 8.2
# 1. Define a class called Address that has two attributes: number and street name. Make sure you have an
# init method that initializes the object appropriately. You do not need to define any other methods.
#
# class Address():
#     def __init__(self, number, str_name):
#         self.number = number
#         self.str_name = str_name


# 2. Consider the following code
# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#
#     def print_time(self):
#         time = "6:30"
#         print(self.time)
# clock = Clock("5:30")
# clock.print_time()
# (a) What does the code print out? Guess first, and then create a Python file and run it. (5:30)
# (b) Why does the code print this? (bc def print_time dont change time (must be self.time),
# print(self.time) only return obj's attribute 5:30)


# 3. Consider the following code:
# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self, time):
#         print(time)
# clock = Clock("5:30")
# clock.print_time("10:30")
# (a) What does the code print out? Guess first, and then create a Python file and run it. 10:30
# (b) What does this tell you about giving parameters the same name as object attributes? We should use different name


# 4. Consider the following code:
# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self):
#         print(self.time)
# boston_clock = Clock("5:30")
# paris_clock = boston_clock
# paris_clock.time = "10:30"
# boston_clock.print_time()
# (a) What does the code print out? Guess first, and then create a Python file and run it. 10:30
# (b) Why does it print what it does? (Are boston clock and paris clock different objects? Why or why
# not?) Same object


class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.incantation  + " " + self.name + "\n" + self.get_description()

    def get_description(self):
        return "No description"

    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, "Accio", "Summoning Charm")
    def get_description(self):
        return "This charm summons an object to the caster, potentially over a significant distance."


class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, "Confundo", "Confundus Charm")

    def get_description(self):
        return "Causes the victim to become confused and befuddled."


def study_spell(spell):
    print(spell)


spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())

# 1. What are the parent and child classes? parent:
# Spell, child: Accio, Confundo

# 2. What does the code print out? (Try figuring it out without running it in Python first)
# Accio
# Summoning Charm Accio
# No description
# Confundus Charm Confundo
# Causes the victim to become confused and befuddled.


# 3. Which get description method is called when ‘study spell(Confundo())’ is executed? Why?
# get_description in the Confundo Class, I think when there are existed methods in both parent an child, those in child class will override

# 4. What do we need to do so that ‘print Accio()’ will print the appropriate description?
# Accio Summoning Charm
# This charm summons an object to the caster, potentially over a significant distance.
# Write down the code that we need to add and/or change.
