
person = {'name': 'Jan', 'age': 23}

# sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
# print(sentence)

# sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
# print(sentence)

# sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
# print(sentence)

# sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
# print(sentence)
#
# l = ['Jan', 23]

# sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(l)
# print(sentence)

# tag = 'h1'
# text = 'This is a headline'

# sentence = '<{0}>{1}</{0}>'.format(tag, text)
# print(sentence)

class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jacek', '33')


import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

# print(my_date)

# March 01, 2016

# sentence = '{:%d %B %Y}'.format(my_date)
#
# print(sentence)

# 01 March, 2016 fell on a Tuesday and was the 061 day of the year.

sentence = '{0:%d %B %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)

print(sentence)