import math

class  Figure:
    sides_count = 0
    def __init__(self, color, *sides, filled = False):
        self.__color = color
        self.__sides = None
        self.set_sides(*sides)
        self.filled = filled

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        valid_values = (0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255)
        valid_type = isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
        return valid_values and valid_type

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    @staticmethod
    def __is_valid_sides(*sides):
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
            return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)      # здесь len от фигуры, он возвращает перимерт фигуры

    def set_sides(self, *new_sides):
        if self.__sides is None:
            self.__sides = [1] * self.sides_count
        valid_sides = []
        for side in new_sides:
            if self.__is_valid_sides(side):
                valid_sides.append(side)
        if len(valid_sides) == len(new_sides) and len(valid_sides) == self.sides_count:
            self.__sides = valid_sides                   # len от кортежа, кол-во элементов в кортеже

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, length, filled = False,):
        super().__init__(color, length, filled = filled)
        self.__radius = length / (2 * math.pi)
    def get_square(self):
        return len(self) ** 2 / (4 * math.pi)               # возвращает площадь круга

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides, filled = False):
        super().__init__(color, *sides, filled = filled)
    def get_square(self):
        p = len(self) / 2
        sides = self.get_sides()
        return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side, filled=False):
        sides = tuple([side] * 12)
        super().__init__(color, *sides, filled=filled)
    def get_volume(self):
        return self.get_sides()[0] ** 3


#Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# print(cube1.get_sides())

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Непредусмотренные проверки
# tr1 = Triangle((200, 200, 100), 10, 6, 4)
# print(tr1.get_sides())
# tr1.set_sides(10,6,-5)
# print(tr1.get_sides())
# tr1.set_sides(10,6,-5,2)
# print(tr1.get_sides())