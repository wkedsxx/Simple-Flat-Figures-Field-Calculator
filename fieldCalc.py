from gi.repository import Gtk
import math

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Field Calculator")
        self.set_border_width(10)

        # Main Box Layout
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        self.add(vbox)
        
        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(500)

        # Square
        listBoxSquare = Gtk.ListBox()
        listBoxSquare.set_selection_mode(Gtk.SelectionMode.NONE)
        
        row1Square = Gtk.ListBoxRow()

        labelSquareSide = Gtk.Label()
        labelSquareSide.set_text("Square side:")

        entrySquareSide = Gtk.Entry()

        hbox1Square = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        hbox1Square.pack_start(labelSquareSide, True, True, 0)
        hbox1Square.pack_start(entrySquareSide, True, True, 0)
        row1Square.add(hbox1Square)
        
        listBoxSquare.add(row1Square)

        row2Square = Gtk.ListBoxRow()
        hbox2Square = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        calcSquare = Gtk.Button.new_with_label("Calculate")
        
        hbox2Square.pack_start(calcSquare, True, True, 0)
        row2Square.add(hbox2Square)

        listBoxSquare.add(row2Square)

        row3Square = Gtk.ListBoxRow()
        hbox3Square = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        labelResultSquare = Gtk.Label()
        labelResultSquare.set_text("0")
        hbox3Square.pack_start(labelResultSquare, True, True, 0)
        row3Square.add(hbox3Square)

        listBoxSquare.add(row3Square)

        stack.add_titled(listBoxSquare, "Square", "Square")

        calcSquare.connect("clicked", self.calcSquareField, entrySquareSide, labelResultSquare)

        # Rectangle
        listBoxRect = Gtk.ListBox()
        listBoxRect.set_selection_mode(Gtk.SelectionMode.NONE)
        
        row1Rect = Gtk.ListBoxRow()

        labelRectSideA = Gtk.Label()
        labelRectSideA.set_text("Rectangle side a:")

        entryRectSideA = Gtk.Entry()

        hbox1RectSideA = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        hbox1RectSideA.pack_start(labelRectSideA, True, True, 0)
        hbox1RectSideA.pack_start(entryRectSideA, True, True, 0)
        row1Rect.add(hbox1RectSideA)
        
        listBoxRect.add(row1Rect)


        row2Rect = Gtk.ListBoxRow()

        labelRectSideB = Gtk.Label()
        labelRectSideB.set_text("Rectangle side b:")

        entryRectSideB = Gtk.Entry()


        hbox2RectSideB = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        hbox2RectSideB.pack_start(labelRectSideB, True, True, 0)
        hbox2RectSideB.pack_start(entryRectSideB, True, True, 0)
        row2Rect.add(hbox2RectSideB)
        
        listBoxRect.add(row2Rect)

        row3Rect = Gtk.ListBoxRow()
        hbox3Rect = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        calcRect = Gtk.Button.new_with_label("Calculate")
        
        hbox3Rect.pack_start(calcRect, True, True, 0)
        row3Rect.add(hbox3Rect)

        listBoxRect.add(row3Rect)

        row4Rect = Gtk.ListBoxRow()
        hbox4Rect = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        labelResultRect = Gtk.Label()
        labelResultRect.set_text("0")
        hbox4Rect.pack_start(labelResultRect, True, True, 0)
        row4Rect.add(hbox4Rect)

        listBoxRect.add(row4Rect)

        stack.add_titled(listBoxRect, "Rectangle", "Rectangle")
        
        calcRect.connect("clicked", self.calcRectField, entryRectSideA, entryRectSideB, labelResultRect)

        # Triangle
        listBoxTriangle = Gtk.ListBox()
        listBoxTriangle.set_selection_mode(Gtk.SelectionMode.NONE)
        
        row1Triangle = Gtk.ListBoxRow()

        labelTriangleSide = Gtk.Label()
        labelTriangleSide.set_text("Triangle side:")

        entryTriangleSide = Gtk.Entry()

        hbox1TriangleSide = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        hbox1TriangleSide.pack_start(labelTriangleSide, True, True, 0)
        hbox1TriangleSide.pack_start(entryTriangleSide, True, True, 0)
        row1Triangle.add(hbox1TriangleSide)
        
        listBoxTriangle.add(row1Triangle)


        row2Triangle = Gtk.ListBoxRow()
        labelTriangleH = Gtk.Label()
        labelTriangleH.set_text("Triangle height:")
        entryTriangleH = Gtk.Entry()

        hbox2TriangleH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        hbox2TriangleH.pack_start(labelTriangleH, True, True, 0)
        hbox2TriangleH.pack_start(entryTriangleH, True, True, 0)
        row2Triangle.add(hbox2TriangleH)
        
        listBoxTriangle.add(row2Triangle)


        row3Triangle = Gtk.ListBoxRow()
        hbox3Triangle = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        calcTriangle = Gtk.Button.new_with_label("Calculate")
        
        hbox3Triangle.pack_start(calcTriangle, True, True, 0)
        row3Triangle.add(hbox3Triangle)

        listBoxTriangle.add(row3Triangle)


        row4Triangle = Gtk.ListBoxRow()
        hbox4Triangle = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        labelResultTriangle = Gtk.Label()
        labelResultTriangle.set_text("0")
        hbox4Triangle.pack_start(labelResultTriangle, True, True, 0)
        row4Triangle.add(hbox4Triangle)

        listBoxTriangle.add(row4Triangle)

        stack.add_titled(listBoxTriangle, "Triangle", "Triangle")

        calcTriangle.connect("clicked", self.calcTriangleField, entryTriangleSide, entryTriangleH, labelResultTriangle)

        # Circle
        listBoxCircle = Gtk.ListBox()
        listBoxCircle.set_selection_mode(Gtk.SelectionMode.NONE)

        row1Circle = Gtk.ListBoxRow()

        labelCircleRadius = Gtk.Label()
        labelCircleRadius.set_text("Circle radius:")
        entryCircleRadius = Gtk.Entry()

        hbox1Circle = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        hbox1Circle.pack_start(labelCircleRadius, True, True, 0)
        hbox1Circle.pack_start(entryCircleRadius, True, True, 0)
        row1Circle.add(hbox1Circle)
        
        listBoxCircle.add(row1Circle)

        row2Circle = Gtk.ListBoxRow()
        hbox2Circle = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        calcCircle = Gtk.Button.new_with_label("Calculate")
        
        hbox2Circle.pack_start(calcCircle, True, True, 0)
        row2Circle.add(hbox2Circle)

        listBoxCircle.add(row2Circle)

        row3Circle = Gtk.ListBoxRow()
        hbox3Circle = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        labelResultCircle = Gtk.Label()
        labelResultCircle.set_text("0")
        hbox3Circle.pack_start(labelResultCircle, True, True, 0)
        row3Circle.add(hbox3Circle)

        listBoxCircle.add(row3Circle)

        stack.add_titled(listBoxCircle, "Circle", "Circle")

        calcCircle.connect("clicked", self.calcCircleField, entryCircleRadius, labelResultCircle)

        # Stack Switcher
        
        figureSwitcher = Gtk.StackSwitcher()
        figureSwitcher.set_stack(stack)

        vbox.pack_start(figureSwitcher, True, True, 0)
        vbox.pack_start(stack, True, True, 0)
        


    def calcSquareField(self, button, side, result):
        self.side = side.get_text()
        self.field = int(self.side) ** 2
        result.set_text(str(self.field))

    def calcRectField(self, button, sideA, sideB, result):
        self.sideA = sideA.get_text()
        self.sideB = sideB.get_text()
        self.field = int(self.sideA) * int(self.sideB)
        result.set_text(str(self.field))
    
    def calcTriangleField(self, button, side, height, result):
        self.side= side.get_text()
        self.height = height.get_text()
        self.field = (int(self.side) * int(self.height)) / 2
        result.set_text(str(self.field))
    
    def calcCircleField(self, button, radius, result):
        self.radius = radius.get_text()
        self.field = math.pi * (int(self.radius) ** 2)
        result.set_text(str(self.field))



window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()