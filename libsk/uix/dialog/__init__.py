from ..ripple import RippleButton
import os.path
from kivy.resources import resource_add_path
from kivy.metrics import dp
resource_add_path(os.path.dirname(__file__))
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
Builder.unload_file("dialog.kv")
Builder.load_file("dialog.kv")
from libsk.uix.sparator import SparatorVertical,SparatorHorizon
from kivy.properties import StringProperty,ListProperty,NumericProperty
class ConfirmationDialog(FloatLayout):
    __event__=("on_positive_statement","on_negative_statement","on_dismiss")
    dialog_text=StringProperty("Write K-line\n SupraX 125 \n 38770-K15-901")
    positive_text=StringProperty("Yes")
    negative_text=StringProperty("Cancel")
    negative_color=ListProperty([0,0,0,1])
    positive_color=ListProperty([0,.5,1,1])
    def __init__(self, **kwargs):
        super(ConfirmationDialog,self).__init__(**kwargs)
def on_positive_statement(self):
    pass
def on_negative_statement(self):
    pass
def on_dismiss(self):
    pass
def dismiss(self):
    self.parent.remove_widget(self)