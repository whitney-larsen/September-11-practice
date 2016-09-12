# name = ("happy").lower()

# letter_count = {}

# for i in range(0,len(name)):
# 	if name[i] in letter_count:	
# 		letter_count[name[i]] = letter_count[name[i]]+1
# 	else: 
# 		letter_count[name[i]] = 1

# print letter_count

# prices = {"banana":4, "apple": 2, "orange": 5, "pear": 3}
# max_price = 0.0
# max_key = ""

# for key,value in prices.items():
# 	if value >= max_price:
# 		max_price = value
# 		max_key = key

# print max_key

employee = {}

employee["name"] = "Whitney"
employee["age"] = 28
employee["height"] = int(raw_input("What is Whitney's height in inches?"))

print employee

employee["age"] = 29

if ("name" in employee) == True:
	print "Name:  " + employee["name"]
else:
	print "The name does not exist"

if (26 in employee) == True:
	print "26:  " + employee[26]
else:
	print "26 does not exist"

for key in employee:
	print key

print employee.keys()

for key, value in employee.items():
	print key, value

print employee.items()

