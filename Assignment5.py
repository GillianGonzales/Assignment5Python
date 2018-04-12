#
#
# Created By Gillian Gonzales
# Created On April 11 2018
#
# This program will ask your age and will tell if your a adult or a kid

print("Type your age ")

user = input()
age = "16"

while True:
	if user <= age:
		print("Your a Kid")
		user = input()
	elif user > age:
		print("Your a adult")
		user = input()
	else:
		print ("Invaild answer")
		user = input 
	pass
pass


	 