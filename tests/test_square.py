import pytest
from square import Square

@pytest.mark.square
def test_square_area_and_perimeter_integers():
    sqr = Square(3)

    assert sqr.get_area() == 9
    assert sqr.get_perimeter() == 12


@pytest.mark.square
def test_square_area_and_perimeter_floats():
    sqr = Square(3.5)

    assert sqr.get_area() == 3.5 * 3.5
    assert sqr.get_perimeter() == 4 * 3.5


@pytest.mark.square
@pytest.mark.parametrize("side_a", [-1, 0])
def test_square_sides_must_be_positive(side_a):
    with pytest.raises(ValueError):
        Square(side_a)
