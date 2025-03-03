print("=======================================================")
print()
print()
print()
print("\t\tWelcome to my Site⁉🌐🌐🌐 \t\t")
print("=======================================================")
print("📝Please \t Signup \t Your Account📝")
print("----------------------------------------------------------")
name = input("Enter Your Name :")
email =input("Enter your email :")
print("Enter Your Gender")
print("-----------------")
print("1. Male")
print("2. Female")
print("3. Others")

# list

# flag = True
# while flag:
#     gender = int(input("Your Choice(Choose one out of three. 1 or 2 or 3) :"))
#     if(gender == 1):
#         flag = False
       
        
#     elif(gender == 2):
#         flag = False
        
        
#     elif(gender == 3):
#         flag = False
       
        
#     else:
#         flag = True
    
gender = ''
while gender not in ['1','2','3']:
    gender = input("Your Choice(Choose one out of three. 1 or 2 or 3) :")
        

import getpass



# pas = input("Enter your password :")
pas = getpass.getpass(prompt='Enter your Password :',stream=SystemError)
# cpas = input("Confirm Your Password :")
cpas = getpass.getpass(prompt='Confirm Your Password :')

import time

if pas != cpas:
    print("Password doesn't match")
else:
    for i in range(1,30):
        print("We are creating Your Account. Plz Wait.")
        time.sleep(1)
    print("Done")   



