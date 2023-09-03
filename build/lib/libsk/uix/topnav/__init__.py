import os.path
from kivy.resources import resource_add_path
resource_add_path(os.path.dirname(__file__))
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty,ColorProperty,ListProperty
from kivy.lang.builder import Builder
Builder.unload_file("topnav.kv")
Builder.load_file("topnav.kv")
class TopNav(BoxLayout):
    source=StringProperty("")
    background_color=ColorProperty([1,1,1,1])
    def __init__(self, **kwargs):
        super(TopNav,self).__init__(**kwargs)

