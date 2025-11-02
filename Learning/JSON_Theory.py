

# What is JSON? JSON - Javascript object notation
# JSON - like dictionary in Python

# How to convert JSON -> Dict

import json

# IMPORTANT: You NEED to use ' ' outside of it, and " inside of the dictionary in json
json_str = '{"id":235, "brand": "Nike,"qty":84, "status":{"isForSale":true}}'

sneakers = json.loads(json_str) # loads - attribute class JSON, and it's an atrribute module class
 # so when we're calling this method .loads - we're calling json string

print(type(sneakers)) # <class 'dict'>

print(sneakers['brand']) #Nike
print(sneakers['qty']) #84
print(sneakers['status']['isForSale']) #True

# How to convert Dict -> JSON
json.dumps(sneakers)  # we're giving JSON dict what is in this example
json.dumps(sneakers, indent=1) # indent - also put spaces
