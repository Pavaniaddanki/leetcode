
##Two sum 

def twosum(i,s):
    print("The sum need to be checked is {}".format(s))
    print("The array entered is {}".format(i))
    
    
lst = []
n = int(input("Enter the number of elements"))
print("Enter the elements")
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
    
print("Array entered by user is {}".format(lst))

s = int(input("Enter the sum which needs to be checked"))

for i in lst:
    j = s-i 
    if j in lst:
        print(i.index,j.index)

twosum(lst,s)
