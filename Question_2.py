# Read a full name and interpret first name, middle name and last name seprated by single or more contiguousspaces. Exceptions need to be processed.

def name(names):
    fullname = names.split()
    try:
        if len(fullname) < 3:
            print("First Name: " ,fullname[0])
            print("Last Name: ", fullname[1])
        else:
            print("First Name: " ,fullname[0])
            print("Middle Name: " ,fullname[1])
            print("Last Name: ", fullname[2])
    except Exception as e:
        print(e)

name("Sandeep Sharma")