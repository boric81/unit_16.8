from rectangle import Rectangle, Square, Circle

rect1=Rectangle(4,5)
rect2=Rectangle(3,5)
print(rect1.get_area())
print(rect2.get_area())

square1=Square(5)
square2=Square(9)

print(square1.get_area_square(),square2.get_area_square())

circle=Circle(6)
print(circle.get_area_circle())

figures=[rect1, rect2, square1, square2, circle]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())

    else:
        print(figure.get_area())
