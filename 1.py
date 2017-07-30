sizes = [2, 7, 9, 30, 35, 40, 45]
b=0
a=1
for i in range(6):
    print("your sizes are: ", sizes)
    index = sizes.index(max(sizes))
    print("your biggest size is: ", sizes[index])
    sizes[index] = 8
    print ("after shearing, your sizes are now: ", sizes)

    for i in range(7):
        sizes[i]= sizes[i] + 50
    print ("after 1 month, my flock is now: ", sizes)
    print("")
    

    print("MONTH", a)
    a=a+1
    print("")

print("i'm bored, i'm gonna sell them all in this month.")
for i in range(7):
    b=b+sizes[i]
print("now my total size is: ", b)
c = b*2
print("i would sell them all for: ",c,"$")
