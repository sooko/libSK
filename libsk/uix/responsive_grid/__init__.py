from kivy.lang.builder import Builder
from kivy.uix.scrollview import ScrollView
import os.path
from kivy.resources import resource_add_path
resource_add_path(os.path.dirname(__file__))
Builder.unload_file("responsive_grid.kv")
Builder.load_file("responsive_grid.kv")
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
class ResponsiveGrid(GridLayout):
    def __init__(self, **kwargs):
        super(ResponsiveGrid,self).__init__(**kwargs)
        