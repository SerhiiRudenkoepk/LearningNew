# We can slice a specific part of our dictionary

alphabet = ["a", "b", "c", "d", "e", "f"]
alphabet_tuples = ("ac", "bs", "cq", "de", "er", "fa")

print(alphabet[2:4])
# Output: c, d.  It starts from C and goes to 4th symbol but not taking it.

print(alphabet[3:])
# Output: d, e, f. We're slicing starting the third symbol and to the end.

print(alphabet[2:5:2])
# Output: c, e. Because we're taking every second symbol from our slice.
# [from which index we're starting slicing : to which index we're slicing : which index we're taking in our group ]
# For tuples it works the same way
print(alphabet_tuples[2:4])
# Output: cq, de