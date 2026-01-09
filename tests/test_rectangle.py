import pytest

from rectangle import Rectangle



@pytest.mark.rectangle
@pytest.mark.parametrize(
    "side_a, side_b, expected_area, expected_perimeter",[(3, 5, 15, 16),(3.5, 5.5, 3.5 * 5.5, 2 * (3.5 + 5.5)),],)
def test_rectangle_area_and_perimeter(side_a, side_b, expected_area, expected_perimeter):
    rect = Rectangle(side_a, side_b)

    assert rect.get_area() == expected_area
    assert rect.get_perimeter() == expected_perimeter



@pytest.mark.rectangle
@pytest.mark.parametrize("side_a, side_b", [(0, 5), (-1, 5), (5, 0), (5, -1)])
def test_rectangle_sides_must_be_positive(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)
