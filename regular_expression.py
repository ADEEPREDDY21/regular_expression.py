print("Example for regular expression")
print("Checking whether email is valid or invalid")
import re
def is_valid_email(email):
    pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern,email):
        return True
    else:
        return False
if __name__=="__main__":
    email=input("Enter an email address:")    
    if is_valid_email(email):
        print(f"The email '{email}' is valid.")
    else:
        print(f"The email '{email}' is not valid.")

print("Example 2 for regular expression")        
print("Checking whether password is valid or invalid")
import re
flag=0
password =input("Enter password:")

while True:
    if len(password)<=8:
        flag=-1
        break
    elif not re.search("[a-z]",password):
        flag=-1
        break
    elif not re.search("[A-Z]",password):
        flag=-1
        break
    elif not re.search("[0-9]",password):
        flag=-1
        break
    elif not re.search("[-@#$]",password):
        flag=-1
        break
    else:
        flag=0
        print("valid password")
        break
if flag==-1:
    print("You entered a invalid password")    
        

    
        