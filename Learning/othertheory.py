# list (it can be changed)
a = []
a.append(1) # add 1 to the list
a.append("abc")
a.append(True)
a.clear() # clean list

# tuples (it can't be changed/edited)
b = (2, "abc")
# only .count and .index can be used for tuple
# You can't use append etc.

# dictionary
{"key1": True, "key2": 10}
person = {"name": "Artem"}
>>> person["name"]
'Artem'

# We can't add new vars to the person dictionary through .append. But we can add it like this:
person["happy"] = True;
# we added new one to the dict. (through the python console)
# We can also change it to something else with the same method:
person["happy"] = False;

# How to copy from one dict to another
new_person = person.copy()


# set - unorganised list of elements without index. It includes only unique elements.
# it can be changed.
# ONCE AGAIN: SET DOESN'T HAVE INDEX
my_fruits = {'apple', 'banana', 'cherry'}
posts_ids = {123, 321, 312}
user_inputs = {True, 1, 'hi'} # in set there's only a set of elements to compare to other.
# but most of the time no one does a set of different elements.


'''
ZIP
ZIP function let us combine 2 lists into one
'''

fruits = ['apple', 'banana', 'cherry']
quantities = [1, 2, 3]

fr_qt_zip = zip(fruits, quantities)
print(fr_qt_zip)
>>> [('apple', 1), ('banana', 2), ('cherry', 3)]
# FYI: that if the len of one list will be higher than another, zip will not add elements what will not have a pair.
# zip can also be converted to dict. But it should only have 2 sequ. (e.g, fruits and quantities (but nothing more than that))
fr_qt_dict = dict(fr_qt_zip)

'''
about for in cycle.
We can use a short version of it.
'''
all_nums = [1, -3, 2]
absol_nums = []

for i in all_nums:
    absol_nums.append(abs(i))

# But we can do it shorter like this:
abs_num = [abs(i) for i in all_nums]
# in the beginning we're using what we want to do, and then write the main part of for in
# OR
abs_num = [i for i in all_nums if i > 0]
# we're adding every number what is higher than 0