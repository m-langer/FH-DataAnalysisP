class Rocket:
    x = 0
    y = 0
    z = 0

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
    
    def move_up(self):
        self.z +=1

space_rockets = []
space_rockets.append(Rocket())
space_rockets.append(Rocket())
space_rockets.append(Rocket())
print(Rocket())

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    finally:
        print("executing finally clause")
divide(2, 1)
# result is 2.0
# executing finally clause
divide(2, 0)