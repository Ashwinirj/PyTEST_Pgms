def color_decorator(func):
    def inside(*args, **kwargs):
        return "Yellow"
    return inside

@color_decorator
def Painter(color):
    color = "Green"
    return color

print(Painter("Red"))