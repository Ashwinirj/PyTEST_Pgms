#dictionary are key value pairs, which are un-ordered and are mutable in nature
# un-ordered -as can be accessed using keys 
# mutable - can be changed at any point
#keys should be unique, and will have integer, float, string,tuple
#values can be of any type and can be duplicate

# ************************************************************************************

D= {1:"Ash", 
    "value":"good", 
    (1,2,3,4):"this is a tuple"}

# D1 = dict(10:"folat","dict":"dict() type")
# print(D1)
D2 = dict([(1,"Hi"),(2,"Hello")])
# print(D2)

# # ****************************************************************
# print(D2[1])
# print(D2.get(1))

emp = {"QA": "Ashwini","Dev": {"dev1":"Deepak","dev2":"Nivaan"} }
# print(emp)
# print(emp["Dev"])
# print(emp.get("Dev").get("dev2"))

emp["manager"] = "Smita"
emp["manager1"] = "Smita"
emp["manager2"] = "Sai"
print(emp)