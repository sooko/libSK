from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.properties import StringProperty,ListProperty,ColorProperty,NumericProperty
Builder.load_string("""
<SparatorHorizon>:
    size_hint: 1, None
    height: dp(1)
    canvas:
        Color:
            rgba:root.color
        Line:
            points:self.x+self.padding,self.y,self.right-self.padding,self.y
<SparatorVertical>:
    size_hint: None,1
    width:dp(1)
    canvas:
        Color:
            rgba:root.color
        Line:
            points:self.x,self.y+self.padding,self.x,self.top-self.padding

                    
""")
class SparatorVertical(Widget):
    color=ColorProperty([1,1,1,1])
    padding=NumericProperty(0)

class SparatorHorizon(Widget):
    padding=NumericProperty(0)
    color=ColorProperty([1,1,1,1])


