name = input("What is your Name: \n")
print("Hello " + name)

objectsList = ["h",2, 2.1, ["hello",0.6],"to Be removed"]
print(objectsList [3][1])

objectsList.pop(4)
print(objectsList)

myTuple =("1", 2, "three",2.9999999)
print(myTuple[2])
print(float(myTuple[0]))
print(int(myTuple[3]))

a = 234
b= "656.454"

print(a + int(float(b)))
print(str(a) + b)

def addString(str_1,str_2):
        try:
            return(str_1 + str_2)
        except :
            return "invalid addition attempt"


a = addString(None, " World")

print(a)
print("End of Program")

