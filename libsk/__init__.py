from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
from .uix.responsive_grid import ResponsiveGrid
from .uix.dialog import ConfirmationDialog
import os.path
from kivy.resources import resource_add_path
resource_add_path(os.path.dirname(__file__))
Builder.unload_file("libsk.kv")
Builder.load_file("libsk.kv")
from libsk.uix.toast import Toast
from .shape import LibskEllipse
from .menus import GridMenu,MenuItemTextBesideIcon
class LibSK(FloatLayout):
    menu_item=MenuItemTextBesideIcon
    def __init__(self, **kwargs):
        super(LibSK,self).__init__(**kwargs)


