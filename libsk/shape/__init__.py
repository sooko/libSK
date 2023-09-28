from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
import os.path
from kivy.resources import resource_add_path
resource_add_path(os.path.dirname(__file__))
Builder.unload_file("shape.kv")
Builder.load_file("shape.kv")
from kivy.properties import StringProperty,NumericProperty,ListProperty,ColorProperty


class LibskEllipse(Widget):
    rotate_angle=NumericProperty(0)
    angle_start=NumericProperty(0)
    angle_end=NumericProperty(360)
    color=ColorProperty([1,1,1,1])
    source=StringProperty("")
    def __init__(self, **kwargs):
        super(LibskEllipse,self).__init__(**kwargs)

from kivy.uix.floatlayout import FloatLayout
class LibskSquare(FloatLayout):
    color=ColorProperty([1,1,1,1])
    source=StringProperty("")
    scale=NumericProperty(1)
    def __init__(self, **kwargs):
        super(LibskSquare,self).__init__(**kwargs)