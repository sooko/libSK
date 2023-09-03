import os.path
from kivy.resources import resource_add_path
resource_add_path(os.path.dirname(__file__))
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringPorperty,ColorProperty,ListProperty
class TopNav(BoxLayout):
    source=StringPorperty("")
    def __init__(self, **kwargs):
        super(TopNav,self).__init__(**kwargs)
        
