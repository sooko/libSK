from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.properties import StringProperty,ListProperty,ColorProperty,NumericProperty
from kivy.resources import resource_add_path
from kivy.metrics import dp
import os.path
resource_add_path(os.path.dirname(__file__))
Builder.unload_file("sparator.kv")
Builder.load_file("sparator.kv")

class SparatorVertical(Widget):
    color=ColorProperty([1,1,1,1])
    padding=NumericProperty(0)

class SparatorHorizon(Widget):
    padding=NumericProperty(0)
    color=ColorProperty([1,1,1,1])


