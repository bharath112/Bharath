#Dictionary is KVP mechanism
# d = {1:"ONE", 2:"TWO", 3:"THREE"}
#e = {"India":}

# l = [1,2,3,4,5]
# print(d[1])
# d[1] = "SEVEN"
# print(d[1])
# d[4] = "FOUR"
# print(d[4])

# print(d.keys())
# print(d.values())
# print(d.items())

#****************
# e = {}
#
# for k,v in d.items():
#     print(k,v)
#     e[v] = k
#
# print(e.items())
#**********************
#
# k = [1,2,3]
# v = ["ONE","TWO","THREE"]
# #d = {}
#
# for i in range(len(k)):
#     d[k[i]] = v[i]
#
# print(d.items())
#
# # print(dict(zip(k,v)))
# #
# # print(list(zip(k,v)))
#
# print(list(zip(*d.items())))

#*******************************
# IPL = {"RCB":["VK","MSD"],"RR":["ST","VS"]}
#
# # print(IPL.items())
# #
# # print(IPL["RCB"][::-1])
# IPL = {"India":{"test":1, "ODI":2}, "England":{"test":2,"ODI":4}}
# print(IPL.items())
# print(IPL["India"]["ODI"])
# #print(IPL.values()[0]["ODI"])   -- it will not work as it is class
# ***************************************
# ask input from user(How many numbers you are entering)
# iterate 5 tiems and store it to list
# after 5, tell how many are even and odd and seggregare them to a dict...
# Result shoudl be below:
# d["sorted"] = store in descen order
# d["even"] = store in even order
# same for odd

# x = input("How number you want to store?")
# list = []
# even = []
# odd = []
# sort_list = []
# dict = {}
#
# for i in range(int(x)):
#     print(i)
#     value = int(input("Enter value:"))
#     list.append(value)
#
# print("Enterd List:")
# print(list)
#
# for num in list:
#     if (num % 2 == 0):
#         even.append(num)
#     else:
#         odd.append(num)
#
# sort_list = sorted(list,reverse=True)
# print("Even Numbers are:")
# print(even)
# print("Odd Numbers are:")
# print(odd)
# print("Sorted List is:")
# print(sort_list)
#
# dict["EVEN"] = even
# dict["ODD"] = odd
# dict["SORT"] = sort_list
#
# print("In a Dict format:")
# print(dict)

#*************Another approach************
# num = int(input("Enter No.of Numbers to store"))
# e = []; o = []; d = {}
# for i in range(num):
#     inp = int(input("Enter Number"))
#     if (inp % 2 == 0):
#         d["Even"] = e.append(inp)
#     else:
#         d["Odd"] = o.append(inp)
#
# sor = sorted(e+o, reverse=True)
#
# d["Sorted"] = sor
#
# print(e);print(o);print(d)


#*****Login page***********
# import getpass
# userdata = {}
# while True:
#     inp = int(input("Enter 1 for Register and 2 for Login and 3 to Exit:"))
#     if inp == 1:
#         UN = input("Enter UserName:").strip()
#         if UN in userdata.keys():
#             print("UserName already exists!")
#         else:
#             userdata[UN] = input("Enter Password:").strip()
#
#         print(userdata)
#     elif inp == 2:
#         UN = input("Enter UserName to Login:").strip()
#         if (UN in userdata.keys()):
#             print("Welcome - ", UN)
#             PW = input("Enter Password:").strip()
#             if (userdata[UN] == PW):
#                 print("Login Successfull!")
#             else:
#                 print("Entered Wrong Password")
#     elif inp == 3:
#         break
#
#     status = int(input("Enter 1 to Continue or 2 to Exit:"))
#     if (status == 1):
#         continue
#     elif (status == 2):
#         break
#
# print(userdata)
# import time
#
# print(time.time())

#************************************
#generate a hotel bill
#menu = {"idli":30, "Dosa":40, "Roticurry":50}

#Quiz - ask two Qs 1. Sceince, 2. Politics, 3. Games
#github.com/kmvinayaka ---- Repo is PythonJupiter
#************************************

menu = {"Idli":25, "Dosa":45, "Idli and Vada":45}
final = {}

print(menu.keys())
print(menu.items())
#print(len(menu))
print("Welcome! - Below are the items available in Hotel:")
print("**************************************************")
j = 1
Len = len(menu)
for item in menu:
    if j <= Len:
        print(j, ".", item, ":", menu[item])

    j += 1

print("**************************************************")
while True:
    str = input("what item you want?")
    if str in menu:
        no = int(input("How many plates you want?"))
        final[str] = no
    else:
        print("your selected item is not in menu! ")

    again = int(input("wanted to have one more item?(1/0)"))
    if again == 1:
        continue
    else:
        break

print(final)
final["Total"] = 0

print("Item ", "NoOf Items", "   Cost")
print("*****************************")
for item in final:
    if item in menu:
        print(item, final[item], menu[item] * final[item])
        hi = menu[item] * final[item]
        final["Total"] += hi

print("*****************************")
print("Total to pay is:", final["Total"])


























