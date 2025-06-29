# 1. Basic syntax 

# #string
# name = "rayees" 
# #integer
# age = 21
# #float
# pi = 3.14

# print(name,age,pi)

# Data types in python:
# A data type is a classification that tells a computer what kind of value a variable can hold, such as a number, text, or true/false.

# Different data types in python: 
# int , float, str, bool, list , tuple , set , dict 


#Type Conversion and casting

# a = int("10") #converting string to int
# b = float("5.6") #convert string to float
# c = str(100) #convert integer to string

# print(a, b, c)



# Dynamic Typing

# x = 5 #int
# x = "Rayee"   #now string


# 2. Operators

# Airthmetic : + - * ? ?? % **
# a = 10
# b = 3
# print(a // b)

# Comparison: == != > < >= <=
# Logical: and, or, not
# Complex Expression


#Lists , Tuples, Sets, Dictionary: 



# /////////////////////////////
#1 The list is a comma-separated item enclosed in square braces. A list is mutable means in the list we can change elements.

# Example of a list
# fruits = ['Orange', 'Apple', 'Pear', 'Banana', 'Kiwi', 'Apple', 'Banana']

# list[0] = "Grape"

# print(fruits)

# Output:
# ['Grape', 'Apple', 'Pear', 'Banana', 'Kiwi', 'Apple', 'Banana']

# Methods performed on lists

# append() - adds an element at the end of the list
# insert() - adds an element at the specified position
# extend() - adds the elements of a list ( or any iterable), to the end of the current list
# copy() - returns a copy of the list
# count() - retuns the number of elements with the specified value
# clear() - removes all the elements from the list
# index() - returns the index of the first element with the specified value
# remove() - removes the item with the specified value
# pop() - removes the order of the list
# reverse() - reverses the order of the list
# sort() - sorts the list


# //////////////////////////
#2 A tuple is also a comma-separated item but enclosed in round braces. A tuple is immutable means in a tuple we can’t change the elements. 

# tuple = ("Chetan","Nitin",23,"Ratan",44)
# tuple[0] = "Shidling"
# print(tuple)

# Output:

# You will get errors like this
# TypeError: 'tuple' object does not support item assigned
# So, in a tuple, we can’t change the element.





#///////////////////////
# Set

# The Set uses the keyword “set” with comma-separated items enclosed with both square & round braces and the set can also be created with curly braces. The set is an unordered collection with no duplicate elements. Curly braces or the set() function can be used to create sets.

# Set with square and round braces
# set = set(["Computer", "Printer", "TV", "Camera", 420])
# print(set)

# Output:

# {'Computer', 'Printer', 'TV', 'Camera', 420}
# It will print output in curly braces.

# Set with curly braces

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana','watermelon'}
# print(basket)
# basket.add('apna fruit')
print(basket)
# type(basket)

# Output:
# {'banana', 'orange', 'apple', 'pear', 'watermelon'}





# //////////////////////
# Dictionary

# A set of key:value pairs – with the requirement that the keys are unique (within one dictionary). dictionaries are indexed by keys, which can be immutable.

# diction_data = {'Name':'Chetan', 'Age':21, 'Height':'5.9 ft', 'Hobby':'Blogging'}
# print(diction_data)
# type(diction_data)

# Output:
# {'Name': 'Chetan', 'Age': 21, 'Height': '5.9 ft', 'Hobby': 'Blogging'}
# dict





# //////////////////////////////////////////////////

### ✅ **Control Structures (Simple Definition):**

# **Control structures** are instructions that decide the **flow of execution** in a program, like making **decisions (if-else)** or **repeating tasks (loops)**.

# > Example:

# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")


# ### ✅ **Dynamic Typing (Simple Definition):**

# **Dynamic typing** means **you don’t need to declare the data type** of a variable. Python automatically understands the type based on the value you assign.

# > Example:

# x = 10      # x is int
# x = "Hello" # now x is str






# //////////////////////////////////////////////////////////


# ### ✅ **Bitwise Operators (Definition):**
# Bitwise operators** are used to perform operations **bit by bit** on integers (binary values). They work directly at the **binary level**.


# ### ✅ **Common Bitwise Operators in Python:**

# | Operator | Name        | Example    | Result (for a = 5, b = 3)   |     |               |               |
# | -------- | ----------- | ---------- | --------------------------- | --- | ------------- | ------------- |
# | `&`      | Bitwise AND | `a & b`    | `1`  → `0101 & 0011 = 0001` |     |               |               |
# | \`       | \`          | Bitwise OR | \`a                         | b\` | `7`  → \`0101 | 0011 = 0111\` |
# | `^`      | Bitwise XOR | `a ^ b`    | `6`  → `0101 ^ 0011 = 0110` |     |               |               |
# | `~`      | Bitwise NOT | `~a`       | `-6` → flips all bits of 5  |     |               |               |
# | `<<`     | Left Shift  | `a << 1`   | `10` → `0101 << 1 = 1010`   |     |               |               |
# | `>>`     | Right Shift | `a >> 1`   | `2`  → `0101 >> 1 = 0010`   |     |               |               |

# ---

# ### ✅ **Example Code:**

# a = 5   # 0101
# b = 3   # 0011

# print("a & b =", a & b)   # 1
# print("a | b =", a | b)   # 7
# print("a ^ b =", a ^ b)   # 6
# print("~a =", ~a)         # -6
# print("a << 1 =", a << 1) # 10
# print("a >> 1 =", a >> 1) # 2


# ✅ What is a Set?

# A **set** is a collection of unique elements (no duplicates), and it's **unordered**.

# **Example:**

# 
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# ---

# ## 🔁 Set Operations:

# ### 1️⃣ **Union (A ∪ B)**

# ➡ Combines elements from both sets without duplicates.

# 
# print(a.union(b))        # OR a | b
# # Output: {1, 2, 3, 4, 5, 6}

# ---

# ### 2️⃣ **Intersection (A ∩ B)**

# ➡ Gets **common** elements from both sets.

# 
# print(a.intersection(b))  # OR a & b
# # Output: {3, 4}

# ---

# ### 3️⃣ **Difference (A - B)**

# ➡ Gets elements in **A that are not in B**.

# print(a.difference(b))    # OR a - b
# # Output: {1, 2}

# > Similarly, `b.difference(a)` will give:

# print(b.difference(a))    # b - a
# # Output: {5, 6}

# ## ✅ Summary Table:

# | Operation    | Symbol | Code                           | Meaning                         |                                    |
# | ------------ | ------ | ------------------------------ | ------------------------------- | ---------------------------------- |
# | Union        | ∪      | \`a                            | b`or`a.union(b)\`               | All unique elements from both sets |
# | Intersection | ∩      | `a & b` or `a.intersection(b)` | Common elements in both sets    |                                    |
# | Difference   | -      | `a - b` or `a.difference(b)`   | Elements only in `a` not in `b` |                                    |

# ---

# ### 🌟 Bonus Tip:

# Sets ignore duplicates automatically:

# 
# s = {1, 2, 2, 3}
# print(s)  # Output: {1, 2, 3}
