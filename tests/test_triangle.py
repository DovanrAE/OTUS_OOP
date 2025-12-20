import pytest
from math import sqrt
from triangle import Triangle


@pytest.mark.triangle
@pytest.mark.parametrize("a,b,c", [(3, 4, 5), (5, 5, 6)])
def test_triangle_area_and_perimeter(a, b, c):
    tr = Triangle(a, b, c)

    expected_perimeter = a + b + c
    p = expected_perimeter / 2
    expected_area = sqrt(p * (p - a) * (p - b) * (p - c))

    assert tr.get_perimeter() == expected_perimeter
    assert tr.get_area() == pytest.approx(expected_area)


@pytest.mark.triangle
@pytest.mark.parametrize("a,b,c", [(0, 4, 5),(-1, 4, 5),(1, 2, 3),(2, 3, 10)])
def test_triangle_rejects_invalid_sides(a, b, c):
    with pytest.raises(ValueError):
        Triangle(a, b, c)
