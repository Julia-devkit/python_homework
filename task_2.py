class Road:
    def __init__(self,length, width):
        self._length = length
        self._width = width
    def whole_mass(self, one_square_miter_mass=25, thickness=5):
        self._mass = one_square_miter_mass
        self._thickness = thickness
        mass = self._length * self._width * self._mass * self._thickness
        return mass
my_mass = Road(100 ,5)
print(my_mass.whole_mass(30, 6))
