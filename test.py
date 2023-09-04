from kivy.uix.floatlayout import FloatLayout
from libsk.uix.carts import Cart
from kivy.lang.builder import Builder
Builder.load_string("""
<Ml>:
    Cart:
        pos_hint: {'center_x': 0.5,'center_y': .5}
        size_hint:.5,.5
    

""")
class Ml(FloatLayout):
    def __init__(self, **kwargs):
        super(Ml,self).__init__(**kwargs)



from kivy.app import App

class Test(App):
    def build(self):
        return Ml()

if __name__=="__main__":
    Test().run()