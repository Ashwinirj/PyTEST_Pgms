def Sum_nums(*args):
    print(sum(args))
    # print(type(args))

def Mul_nums(**kwargs):
    print(kwargs)
    print(type(kwargs))

def employee(*args, **kwargs):
    print(args, kwargs)
    print(f"Marks are {args[0]}")
    print(f"Name is {kwargs['name']}")
    print(f"Salary is {kwargs['sal']}")


Sum_nums(4,8,2,1)
Mul_nums(name="Ash",marks="100")


employee(10,20,30,45.6,name="Ashwini",dept="CS",roll_no=4,sal="1200000")