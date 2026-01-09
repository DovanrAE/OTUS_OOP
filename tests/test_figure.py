import pytest

from rectangle import Rectangle
from square import Square
from circle import Circle


@pytest.mark.figure
@pytest.mark.parametrize("figure_1, figure_2, expected",
                         [(Rectangle(3, 5), Square(5), 40), (Circle(3), Square(3), 37.27),],
                         ids=["Rectangle and Square", "Circle and Square"],)
def test_add_area_positive_rounded(figure_1, figure_2, expected):
    assert figure_1.add_area(figure_2) == pytest.approx(expected, abs=0.01)
