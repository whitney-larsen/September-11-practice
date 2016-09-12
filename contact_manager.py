from Contact import ContactClass

def main():
	contact_list = []
	first_name = raw_input("What is the contact's first name?")
	last_name = raw_input("What is the contact's last name?")
	mobile = raw_input("What is the contact's mobile number")
	email = raw_input("What is the contact's email?")
	new_contact = ContactClass(first_name,last_name,mobile,email)
	contact_list.append(new_contact)

	for i in range(len(contact_list)):
		print contact_list[i].first_name
		print contact_list[i].last_name
		print contact_list[i].mobile
		print contact_list[i].email

if __name__ == '__main__':
	main()