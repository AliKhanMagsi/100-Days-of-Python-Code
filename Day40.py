print("User Profile")
name= input("Enter full name: ")
DOB= input("Enter date of birth: ")
tel= input("Enter telephone number: ")
email= input("Enter valid email: ")
address= input("Enter home address: ")
userDetails= {"name": name, "DOB": DOB, "tel": tel, "email": email, "address": address}

print()
print("Summary")
print("Name: ", userDetails["name"])
print("Date of Birth: ", userDetails["DOB"])
print("Tel no: ", userDetails["tel"])
print("Email: ", userDetails["email"])
print("Address: ", userDetails["address"])
