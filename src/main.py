from graphics import Window
from point import Point
from line import Line


def main():
    win = Window(800, 600)

    # Create some points
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(300, 100)
    p4 = Point(400, 200)
    p5 = Point(500, 300)
    p6 = Point(600, 400)

    # Create some lines
    line1 = Line(p1, p2)
    line2 = Line(p3, p4)
    line3 = Line(p5, p6)

    # Draw the lines
    win.draw_line(line1, "red")
    win.draw_line(line2, "blue")
    win.draw_line(line3, "green")

    win.wait_for_close()


main()
