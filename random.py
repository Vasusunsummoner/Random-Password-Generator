import string 
import random 
passwrd = string.ascii_letters+string.digits+string.punctuation 

numPass = int(input("How many passwords do you need to be generated? "))
length = int(input("Enter the length of the password(s): "))

print("List(s) of Generated passwords: ")

for _ in range(numPass):
    print(''.join(random.sample(passwrd, k=length))) 