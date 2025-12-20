import pytest
from figure import Figure


class EXAMPLE_FIGURE(Figure):
    def __init__(self, area: float, perimeter: float = 0):
        self._area = area
        self._perimeter = perimeter

    def get_area(self):
        return self._area

    def get_perimeter(self):
        return self._perimeter


def test_add_area_returns_sum():
    fig1 = EXAMPLE_FIGURE(10)
    fig2 = EXAMPLE_FIGURE(5)
    result = fig1.add_area(fig2)
    assert result == 15


def test_add_area_rejects_non_figure():
    fig = EXAMPLE_FIGURE(10)
    with pytest.raises(ValueError):
        fig.add_area("not a figure")
