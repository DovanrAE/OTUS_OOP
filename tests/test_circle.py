import pytest
from math import pi
from circle import Circle


@pytest.mark.circle
@pytest.mark.parametrize("radius", [1, 2.5])
def test_circle_area_and_perimeter(radius):
    c = Circle(radius)

    assert c.get_area() == pytest.approx(pi * radius * radius)
    assert c.get_perimeter() == pytest.approx(2 * pi * radius)


@pytest.mark.circle
@pytest.mark.parametrize("radius", [0, -1, -2.5])
def test_circle_rejects_non_positive_radius(radius):
    with pytest.raises(ValueError):
        Circle(radius)
