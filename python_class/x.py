from pykeyboard  import *
from pymouse import *
m = PyMouse()
k = PyKeyboard()
m.click(1157,470)
k.type_string('123456')
k.tap_key(k.enter_key)