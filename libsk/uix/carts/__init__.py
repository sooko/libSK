from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
from kivy.properties import ListProperty,StringProperty,NumericProperty,ColorProperty
from kivy.metrics import dp
import os.path
from kivy.resources import resource_add_path
resource_add_path(os.path.dirname(__file__))

Builder.unload_file("cart.kv")
Builder.load_file("cart.kv")

class Cart(FloatLayout):
    radius=ListProperty([dp(5),dp(5),dp(5),dp(5)])
    offset=ListProperty([0, -10])
    spread_radius= ListProperty([-10, -10])
    border_radius= ListProperty([10, 10, 10, 10])
    blur_radius= NumericProperty(30)
    background_color=ColorProperty([.2,.2,.2,1])
    shadow_color=ColorProperty([1,1,1,1])
    
    def __init__(self, **kwargs):
        super(Cart,self).__init__(**kwargs)
