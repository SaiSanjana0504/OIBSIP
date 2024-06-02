import string
import random
length=int(input("enter the length of the password:"))
if length<1:
    print("password length must be atleast one !")
elif length>=1:
    characters = string.ascii_letters + string.digits + string.punctuation
    password=''.join(random.choices (characters,k=length))
    print(password)
else:
    print ("error! enter a valid length for password ")
