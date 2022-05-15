import polygon_area_calculate
from unittest import main


rect = polygon_area_calculate.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = polygon_area_calculate.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)


# Run unit tests automatically
main(module='test_case', exit=False)