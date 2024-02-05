from graphics import Window, Point, Line


def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(0, 0), Point(300, 100)), "red")
    win.wait_for_close()


main()
