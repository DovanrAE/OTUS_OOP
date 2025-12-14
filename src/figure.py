from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @property
    def area(self):
        return self.get_area()

    @property
    def perimeter(self):
        return self.get_perimeter()

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Should be a Figure")
        return self.get_area() + other_figure.get_area()