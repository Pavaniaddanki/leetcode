def reverse(s):
    str = ""
    for i in s:
        print("i".format(i))
        #print("str".format(str))

        str = i + str 
        print("str".format(str))

    return str



s = "Pavani"

print("Original string is: ",end="")
print(s)

print("The reversed string is :", end="")
print(reverse(s))