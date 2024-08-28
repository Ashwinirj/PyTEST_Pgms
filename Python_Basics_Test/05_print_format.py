# log = " I am learning new language"
# lang = "Python"

# # print(log+lang)
# # print(log+" "+lang)
# print(f"{log} {lang}")
# ------------------------------------------------------------------
# name = "Ashwini"
# _name = "my name is {}".format(name) 
# print(name.format())
# print(_name)
# print(full_name + "Jadhav")

# ------------------------------------------------------------------
template = "Test {name}: {result}"
message = template.format(name="Login", result="Passed")
print(message)

# --------------------------------------------------------------------
fname = "Ashwini"
lname = "Jadhav"
print("my name is {} {} {}".format(fname,lname,"Shinde"))

print("my son name is {} {} {}".format("Nivaan","","Shinde"))
print("my son name is {0} {1} {2}".format("Nivaan","","Shinde"))

print("I love to go out places like {d} {b} {u}".format( d="Dharwad", b="Bengaluru", u="Uchha"))
print("I love to go out places like {u} {d} {b}".format( d="Dharwad", b="Bengaluru", u="Uchha"))
