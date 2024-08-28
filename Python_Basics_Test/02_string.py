name = "   Ashwini    R Jadhav        loves to      code in    Python "
# print( len(name))
# print(name.index("J"))


# print(name.capitalize()) 

# print(name.split(" "))
# # print(len(name.split(" ")))

# print(name.count("a"))
#*****************************************************************************************
# Replaces occurrences of a specified substring with another substring.
# Example: "Hello World".replace("World", "Python") → 'Hello Python'
# print(name.replace('P', "j"))

# print(name.replace('Jadhav', "Shinde"))
#******************************************************************************************
# print(name.lower())
# print(name.upper())

# print(name.title())

#****************************************************
# name1 = name.title()
# print(name1)
# print(name1.capitalize())
#*****************************************************
# Removes any leading and trailing whitespace (or specified characters) from the string.
# Example: " Hello ".strip() → 'Hello'
# name = "aaa Ashwini    R Jadhav        loves to      code in    Python aaaa"
# print(name)
# print(name.strip('a'))
# #***********************************************************************************
# . str.join(iterable)
# Joins the elements of an iterable (e.g., list) into a single string, separated by the string on which join is called.
# Example: " ".join(['Hello', 'World']) → 'Hello World'
# name1 = "Ashwini Jadhav"
# name = ["aaa", "Ashwini"]
# name2 = print("*".join(name1))
# print(name2)

# print("/".join(name))
# *********************************************************************************************
name = "aaa Ashwini    R Jadhav        loves to      code in    Python aaaa P P "

print(name.find('P'))