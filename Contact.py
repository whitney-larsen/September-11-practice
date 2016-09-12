class ContactClass(object):
	def __init__(self,first_name,last_name,mobile="",email=""):
		self.first_name = first_name
		self.last_name = last_name
		self.mobile = mobile
		self.email = email

	def send_text(self,message):
		if self.mobile == "":
			print "There is no mobile number"
		else:
			print "To: " + str(self.mobile) + " - " + message


# def main():
	# contact_list = []
	# contact1 = Contact("Whitney", "Larsen",mobile=9737684277)
	# contact2 = Contact("Philip", "shafnacker",mobile = 5555555555)
	# contact3 = Contact("Audrey","Larsen",email = "camplarsen@comcast.net")

	# contact_list = [contact1, contact2, contact3]
	# for i in range(len(contact_list)):
	# 	print contact_list[i].first_name
	# 	print contact_list[i].last_name
	# 	print contact_list[i].mobile
	# 	print contact_list[i].email
	# 	contact_list[i].send_text("Happy Birthday")


if __name__ == '__main__':
	main()