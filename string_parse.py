# str = "item:apples,quantity:4,price:1.50\n"

# split_string = str.split(",")
# print split_string

# split_string = split_string[2].split(":")
# print split_string

# split_string = float(split_string[1])
# print split_string


# my_name = "Whitney"
# print list(my_name)

# str = "1,2,3,4,5"
# split_string = str.split(",")
# for i in range(len(split_string)):
# 	split_string[i] = int(split_string[i])
# print split_string

# str = "One fish two fish red fish blue fish"
# split_string = str.split(" ")
# print split_string

# grocery_string = "item:apples,quantity:4,price:1.50\n"
# grocery_string_split = grocery_string.split(",")
# print grocery_string_split

# quantity_list = grocery_string_split[1].split(":")
# price_list = grocery_string_split[2].split(":")

# quantity = int(quantity_list[1])
# price = float(price_list[1])

# print quantity
# print price

# total = quantity*price
# print total


items = ["item:apples,quantity:4,price:1.50\n", "item:pears,quantity:5,price:2.00\n", "item:cereal,quantity:1,price:4.49\n"]
total = 0

for i in range(len(items)):
	grocery_string = items[i]
	grocery_string_split = grocery_string.split(",")
	quantity_list = grocery_string_split[1].split(":")
	price_list = grocery_string_split[2].split(":")
	quantity = int(quantity_list[1])
	price = float(price_list[1])
	total = total + quantity*price

print total






