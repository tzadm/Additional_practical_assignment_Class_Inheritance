class Figure:
    side_count = 0

    def __init__(self, rgb, *sides):
        self.__sides = [int(x) for x in sides]
        self.__color = list(rgb)
        if self.side_count == 12 and len(self.__sides) != 1:
            self.__sides = [1 for _ in range(self.side_count)]
        elif self.side_count == 12 and len(self.__sides) == 1:
            self.__sides = [sides[0] for _ in range(self.side_count)]
        if self.side_count == 3 and len(self.__sides) != self.side_count:
            self.__sides = [1 for _ in range(self.side_count)]
        if self.side_count == 1 and len(self.__sides) != self.side_count:
            self.__sides = [1 for _ in range(self.side_count)]
        self.filled = True

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        return ((0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255)
                and (type(r) is int and type(g) is int and type(b) is int))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, sides):
        return ((all(type(x) is int for x in sides)
                 and all(x > 0 for x in sides))
                and len(sides) == self.side_count)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.side_count != 12:
            if self.__is_valid_sides(new_sides):
                self.__sides = list(new_sides)
        elif self.__is_valid_sides(new_sides):
            if all(new_sides[0] == _ for _ in new_sides):
                self.__sides = [new_sides[0] for _ in range(12)]
            else:
                print("Введенные стороны не равны, изменения не приняты !")


class Circle(Figure):
    side_count = 1

    def __init__(self, rgb, *sides):
        super().__init__(rgb, *sides)
        self.__radius = super().get_sides()[0] / (3.13 * 2)

    def get_square(self):
        return (self.__radius ** 2) * 3.14


class Triangle(Figure):
    side_count = 3

    def __init__(self, rgb, *sides):
        super().__init__(rgb, *sides)

    def get_square(self):
        list_ = super().get_sides()
        p = 0.5 * sum(list_)
        return (p * (p - list_[0]) * (p - list_[1]) * (p - list_[2])) ** 0.5


class Cube(Figure):
    side_count = 12

    def __init__(self, rgb, *sides):
        super().__init__(rgb, *sides)


    def get_volume(self):
        return super().get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))
print(cube1.get_volume())
