from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
from .uix.responsive_grid import ResponsiveGrid
import os.path
from kivy.resources import resource_add_path
resource_add_path(os.path.dirname(__file__))
Builder.unload_file("libsk.kv")
Builder.load_file("libsk.kv")
from .menus import GridMenu
class LibSK(FloatLayout):
    def __init__(self, **kwargs):
        super(LibSK,self).__init__(**kwargs)


