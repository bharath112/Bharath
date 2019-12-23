#Prog for Login page
#can = True
# userlist  = list()
# passlist = list()
# while (can == True):
#     UN = input("Enter your name:").strip()
#     PW = input("Enter password:").strip()
#
#     if (UN in userlist) and (PW in passlist):
#         print("Entered duplicate user/password! Try again with diff username")
#     else:
#         print("you are in else condition")
#         userlist.append(UN)
#         passlist.append(PW)
#         can = input("wanted to have one more username?")
#         if (can == False):
#             break
#
# print("Usernames are:", userlist)

#*************************************
# UN = ["KMV", "VMK", "MKV"]
# PW = [123, 456, 789]
#
# x = input("Enter Registered Username:").strip()
#
# if (x in UN):
#     print("Welcome!")
#     y = input("Enter UserName Password")
#     if (y in PW):
#         print("Successfull Login")
#     else:
#         print("Wrong Password")
# else:
#     print("UserName doesn't exists!!")

#***********************************************
mode = int(input("Enter 1 for SignUp, 2 for SignIn:"))
userlist  = list()
passlist = list()

if mode == 1:
    can = True
    while can:
        UN = input("Enter your name:").strip()
        PW = input("Enter password:").strip()

        if (UN in userlist) and (PW in passlist):
            print("Entered duplicate user/password! Try again with diff username")
        else:
            print("you are in else condition")
            userlist.append(UN)
            passlist.append(PW)
            can = input("wanted to have one more username(True/Flase)?")
            if (bool(can==False)):
                break

    print("Usernames are:", userlist)
elif mode == 2:
    x = input("Enter Registered Username:").strip()

    if (x in userlist):
        print("Welcome!")
        y = input("Enter UserName Password")
        if (y in passlist):
            print("Successfull Login")
        else:
            print("Wrong Password")
    else:
        print("UserName doesn't exists!!")

else:
    print("Invalid credentials!!")