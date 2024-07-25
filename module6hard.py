class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled=bool):
        self.__color = list(color)  # список цветов RGB
        self.__sides = [sides for _ in range(self.sides_count)]  # список сторон, int
        self.filled = filled  # не/закрашенный, bool

    def get_color(self):
        print(f'Цвет фигуры (RGB): {self.__color}')  # геттер возвращает список RGB цветов

    @staticmethod
    def __is_valid_color(r, g, b):
        """"статический метод принимает параметры r, g, b, который
        проверяет корректность переданных значений перед установкой
        нового цвета. Корректным цвет: все значения r, g и b - целые числа
        в диапазоне от 0 до 255 (включительно)."""
        return True if 0 < r < 255 and 0 < g < 255 and 0 < b < 255 else False

    def set_color(self, r, g, b):
        """ Данный сеттер принимает параметры r, g, b - числа и изменяет
                атрибут __color на соответствующие значения"""
        if self.__is_valid_color(r, g, b) is True:
            self.__color = [r, g, b]

    def __is_valid_sides(self, my_list):
        """служебный, принимает неограниченное кол-во сторон,
               возвращает True если все стороны целые положительные
               числа и кол-во новых сторон совпадает с текущим"""
        if len(my_list) == self.sides_count:
            for i in my_list:
                if i < 0:
                    return False
            return True
        else:
            return False

    def get_sides(self):
        print(f'Список сторон фигуры: {self.__sides}')   # геттер возвращает списо сторон

    def __len__(self):
        print(f'Периметр фигуры : {sum(self.__sides)}')

    def set_sides(self, *new_sides):
        my_list = [*new_sides]
        """ Данный сеттер принимает неограниченное кол-во сторон,
         проверяет корректность переданных данных"""
        if self.__is_valid_sides(my_list) is True:
            self.__sides = my_list


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color=color, sides=sides)
        self.__radius = sides / (2 * 3.1415)

    def get_square(self):
        print(f'Площадь фигуры (круга): {3.1415 * (self.__radius**2)}') # метод возвращает площадь круга


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color=color, sides=sides)
        self.__sides = sides
        self.__a = self.__sides[0]
        self.__b = self.__sides[1]
        self.__c = self.__sides[2]
        # self.__square = 0

    def get_square(self):
        """" возвращает площадь треугольнька по формуле Герона"""
        p = (self.__a + self.__b + self.__c) / 2
        self.__square = (p*(p - self.__a) * (p - self.__b) * (p - self.__c)) ** 0.5
        print(f'Площадь фиугры (треугольника): {self.__square}')


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color=color, sides=sides)
        self.__sides = sides

    def get_volume(self):
        """возвращает объём куба."""
        print(f'Объем куба: {self.__sides ** 3}')


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
triangle1 = Triangle((122, 35, 234), [10, 4, 7])
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # изменится
circle1.get_color()
triangle1.set_color(10, 20, 39)
triangle1.get_color()   # изменится
cube1.set_color(300, 70, 15)  # Не изменится
cube1.get_color()

# Проверка площади :
circle1.get_square()
triangle1.get_square()

# Проверка объёма (куба):
cube1.get_volume()

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # не изменится
cube1.get_sides()
triangle1.set_sides(8, 4, 6)  # изменится
triangle1.get_sides()
circle1.set_sides(15)  # изменится
circle1.get_sides()

# Проверка периметра :
cube1.__len__()
triangle1.__len__()
circle1.__len__()


