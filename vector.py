from math import hypot

class Vector:

    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vector{(self.x, self.y)}'
    
    def __abs__(self) -> float:
        return hypot(self.x, self.y)
    
    def __bool__(self) -> bool:
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scale):
        return Vector(self.x * scale, self.y * scale)
    
    def __rmul__(self, scale):
        return Vector(self.x * scale, self.y * scale)
    
v1 = Vector(x=0, y=0)
v2 = Vector(x=2,y=3)
# print(v1+v2)
# print(v1 * 2)
# print(2 * v1)

print(bool(v1))