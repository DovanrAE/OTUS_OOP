import pytest

from rectangle import Rectangle



@pytest.mark.rectangle
def test_rectangle_area_and_perimeter_integers():
    rect = Rectangle(3, 5)

    assert rect.get_area() == 15
    assert rect.get_perimeter() == 16

@pytest.mark.rectangle
def test_rectangle_area_and_perimeter_floats():
    rect = Rectangle(3.5, 5.5)

    assert rect.get_area() == 3.5 * 5.5
    assert rect.get_perimeter() == 2 * (3.5 + 5.5)



@pytest.mark.rectangle
@pytest.mark.parametrize("side_a, side_b", [(0, 5), (-1, 5), (5, 0), (5, -1)])
def test_rectangle_sides_must_be_positive(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)
