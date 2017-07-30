listt = ['ember', 'qop','storm']
print("welcome to our shop: ")
print (listt)
while True:
    a= input("here are the command list: crud: ")
    if a == "c":
        c=input("what do you want to create:")
        listt.append(c)
        print(listt)
    elif a=="r":
        print("this is the list in better view")
        for i in listt:
            print(i)
       
    elif a == "u":
        c = input("what do you wanna replace:")
        b = input("change to what?:")
        index = listt.index(c)
        listt[index] = b
        print(listt)
    elif a == "d":
        c=input("what do you want to delete:")
        listt.remove(c)
        print(listt)
