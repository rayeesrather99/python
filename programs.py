#while loop /////////////////////////////////////
# n = 1
# while n < 5:
#     print("The counter is:", n)
#     n = n+1


#function ///////////////////////////////////
# def greetings(name):
#     return "Hello " + name

# result = greetings("Virat")
# print(result)



#recursion of factorial program //////////////////////////////////
# def factorial(n):
#     if n ==1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))



#String operations ////////////////////////
# string = "rayees"

# print(string.upper())
# print(string.lower())
# print(len(string))




# List operations ////////////////////////////////
# myList = [1,2,3,4,5]
# # myList.append(6)
# # myList.remove(2)
# # myList.reverse()
# # myList.insert(3,9)

# for i in myList:
#     print(i)

#smallest and largest number in a list 

# dummyList = [1,2,3,4]
# largest = max(dummyList)
# smallest = min(dummyList)

# print("The largest number in the list is: ", largest, " ", "and the smallest no is:", smallest);

#to check element in a list and this is same for tuple , dict (if we have to print values then variable name . items() is used.)
# newList = [1,2,3,4,5]
# if 9 in newList:
#     print("Yes , it exits")
# else:
#     print("No, it does not exist")



#Palindrome program ////////////////////////////////
# def isPalindrome(originalString):
#     originalString = originalString.lower()
#     reversedString = originalString[::-1]

#     if originalString == reversedString:
#         return "Yes, the string is palindrome!"
#     else:
#         return "No, its not Palindrome"

# result = isPalindrome("MOn")
# print(result)



#Tuple operations ////////////////////////////////

# myTuple = (1, 2, 3, 4, 5)

# Tuples are immutable, so we cannot change their elements
# However, we can access elements using indexing
# print(myTuple[0])  # Accessing the first element
# We can also convert a tuple to a list if we need to modify it
# myList = list(myTuple)
# myList.append(6)  # Adding an element to the list
# myTuple = tuple(myList)  # Converting back to a tuple

# for i in myTuple:
#     print(i)
# lenOfTuple = len(myTuple)
# print(lenOfTuple)





# Sets ////////////////////////////////////////////

# mySet = {1,2,3,4,5}

# mySet.add(6)  # Adding an element to the set
# mySet.remove(2)  # Removing an element from the set
# mySet.remove(2)

# for i in mySet:
#     print(i)





# Dictionary operations ////////////////////////////////
studentDetails = [
    {
        "name": "Rayees",
        "marks": 90
    },
    {
        "name": "Muzamil",
        "marks": 99
    },
    {
        "name": "Ghazi",
        "marks": 95
    }
]

studentDetails[0]["marks"] = 100

#appends a new student to the list
# studentDetails.append({
#     "name" : "newStudent",
#     "marks" : 80
# })

# del studentDetails[3] // deletes the last element
for student in studentDetails:
    print(student)