Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle

>>> turtle.setup(400, 400, 0, 0)

>>> venster = turtle.getscreen()
venster.bgcolor("yellow")

SyntaxError: multiple statements found while compiling a single statement
>>> 
KeyboardInterrupt
>>> venster = turtle.getscreen()
>>> 
venster.bgcolor("yellow")
>>> turtle.reset()
>>> turtle.bgcolor("white")
>>> turtle.pencolor("#00008b")
>>> turtle.fillcolor("00008b")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    turtle.fillcolor("00008b")
  File "<string>", line 8, in fillcolor
  File "C:\Users\akith\AppData\Local\Programs\Python\Python38-32\lib\turtle.py", line 2288, in fillcolor
    color = self._colorstr(args)
  File "C:\Users\akith\AppData\Local\Programs\Python\Python38-32\lib\turtle.py", line 2696, in _colorstr
    return self.screen._colorstr(args)
  File "C:\Users\akith\AppData\Local\Programs\Python\Python38-32\lib\turtle.py", line 1158, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string: 00008b
>>> turtle.fillcolor("00008b")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    turtle.fillcolor("00008b")
  File "<string>", line 8, in fillcolor
  File "C:\Users\akith\AppData\Local\Programs\Python\Python38-32\lib\turtle.py", line 2288, in fillcolor
    color = self._colorstr(args)
  File "C:\Users\akith\AppData\Local\Programs\Python\Python38-32\lib\turtle.py", line 2696, in _colorstr
    return self.screen._colorstr(args)
  File "C:\Users\akith\AppData\Local\Programs\Python\Python38-32\lib\turtle.py", line 1158, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string: 00008b
>>> turtle.fillcolor("#00008b")
>>> turtle.forward(100)
>>> turtle.right(90)
>>> turtle.forward(100)
>>> turtle.undo
<function undo at 0x00F8B610>
>>> turtle.reset
<function reset at 0x00F85F58>
]
>>> turtle.reset()
>>> turtle.forward(100)
>>> turtle.pencolor("#00008b")
>>> turtle.reset()
>>> turtle.pencolor("#00008b")
>>> turtle.fillcolor("#00008b")
>>> turtle.forward(100)
>>> turtle.right(90)
>>> turtle.forward(50)
>>> turtle.right(90)
>>> turtle.forward(200)
>>> turtle.right(90)
>>> turtle.forward(50)
>>> turtle.right(90)
>>> turtle.forwar(100)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    turtle.forwar(100)
AttributeError: module 'turtle' has no attribute 'forwar'
>>> turtle.forward(100)
>>> turtle.begin_fill
<function begin_fill at 0x00F85220>
>>> turtle.bein_fill()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    turtle.bein_fill()
AttributeError: module 'turtle' has no attribute 'bein_fill'
>>> turtle.begin_fill()
>>> turtle.forward(100)
>>> turtle.right(90)
>>> turtle.forward(50)
>>> turtle.right(90)
>>> turtle.forward(200)
>>> turtle.right(90)
>>> turtle.forward(50)
>>> turtle.right(90)
>>> turtle.forward(100)
>>> turtle.end_fill()
>>> turtle.pencolor("white")
>>> turtle.fillcolor("#bf2000")
>>> turtle.left(90)
>>> turtle.forward(50)
>>> turtle.right(90)
>>> turtle.bein_fill()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    turtle.bein_fill()
AttributeError: module 'turtle' has no attribute 'bein_fill'
>>> turtle.begin_fill()
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(50)
>>> turtle.left(90)
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.forward(50)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.end_fill()
>>> 