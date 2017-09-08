x=[1,2,3,4,5,6,7,8,9,0]
empty_list=[]
print(x)
print(empty_list)


#Acccessing Elements inside the links
x.append(11)   #To add file to the last of the x.If the thing is string use double quotes.

x.insert(10,10) #To add file to the desired place

print("x After insterting new element =",x)

y=x.index(3) #Usd to find the index number of the particular item.

print("Index number of x =",y)

z=x.pop() #This will popout last item in the list
print("Popped Item =", z)
print("New List = ",x)

x.remove(5) #Its's remove the desired element


print("x after removing element 5",x)


print()
print("*"*80)

print("Slicing a list")

slicing=x[5:]
print(slicing)


print()
print("*"*80)


x.sort() #Sort the values in x

print(x)