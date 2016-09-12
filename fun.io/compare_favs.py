with open ("Whitney_fav_foods.txt") as my_file:
	Whitney_favs = my_file.readlines()

with open ("Philip_fav_foods.txt") as my_file:
	Philip_favs= my_file.readlines()

def compare_foods (list1, list2):
	if Whitney_favs[0] == Philip_favs[0]:
		print "Our favorite foods are the same!"
	else:
		print "Our favorite foods are different!"

compare_foods(Whitney_favs,Philip_favs)