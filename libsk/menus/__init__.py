from kivy.uix.gridlayout import GridLayout

from kivy.properties import StringProperty,DictProperty,ObjectProperty,ColorProperty,NumericProperty,ListProperty
from kivy.uix.boxlayout import BoxLayout
from libsk.uix.ripple import RippleButton
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.event import EventDispatcher
import os.path
from kivy.metrics import dp
from kivy.resources import resource_add_path
resource_add_path(os.path.dirname(__file__))
from kivy.lang.builder import Builder
Builder.unload_file("menus.kv")
Builder.load_file("menus.kv")
import json
class MenuItem(EventDispatcher):
    icon_color=ColorProperty([1,1,1,1])
    name_color=ColorProperty([1,1,1,1])
    icon_font_name=StringProperty("assets/fonts/ico.ttf")
    name_font_name=StringProperty("assets/fonts/open_sans.ttf")
    icon_font_size=NumericProperty(dp(14))
    name_font_size=NumericProperty(dp(14))
    
    radius=ListProperty([dp(10),dp(10),dp(10), dp(10)])
    __events__=("on_event1","on_event2","on_event3","on_event4","on_press")
    data=DictProperty({
                "module": "apps.hdiag_pro",
                "class": "HDiagPro",
                "icon": "assets/icons/4.png",
                "path": "apps/hdiag_pro",
                "name": "HDiag Pro",
                "version": "2023.0808.2121",
                "url": "apps/hdiag_pro.zip",
                "value": "",
                "action": "Install",
                "category": "Apps",
                "key": "hdiag_pro",
                "short_description": "Remap tool for honda",
                "long_description": "",
                "requirements": []
            })
    def on_press(self):
        pass
    def on_event1(self):
        pass
    def on_event2(self):
        pass
    def on_event3(self):
        pass
    def on_event4(self):
        pass

    
    
class MenuItemTextUnderIcon(FloatLayout,MenuItem):
    # icon_font_name=StringProperty("assets/fonts/ico.ttf")
    pass

class MenuItemTextBesideIcon(FloatLayout,MenuItem):

    pass
    # icon_font_name=StringProperty("assets/fonts/ico.ttf")


class GridMenu(GridLayout):

    __events__=("on_menu_selected","on_event4_selected","on_event3_selected","on_event2_selected","on_event1_selected")
    menu_data=DictProperty({})
    menu_item=ObjectProperty(MenuItemTextUnderIcon)
    item=ObjectProperty()
    data=DictProperty({})

    icon_color=ColorProperty([1,1,1,1])
    name_color=ColorProperty([1,1,1,1])
    icon_font_name=StringProperty("assets/fonts/icon_outline.otf")
    name_font_name=StringProperty("assets/fonts/open_sans.ttf")
    icon_font_size=NumericProperty(dp(14))
    name_font_size=NumericProperty(dp(14))
    menu_file=StringProperty("")


    def __init__(self, **kwargs):
        super(GridMenu,self).__init__(**kwargs)
        
    def on_menu_file(self,a,b):
        f=open(b,"r")
        data=json.load(f)
        self.menu_data=data
        f.close()
    def on_menu_data(self,a,b):
        Clock.unschedule(self.create_menu)
        Clock.schedule_once(self.create_menu,.1)
    def create_menu(self,dt):
        self.clear_widgets()
        for i in self.menu_data:
            self.add_widget(self.menu_item(
                                           icon_color=self.icon_color,
                                           name_color=self.name_color,
                                           icon_font_name=self.icon_font_name, 
                                           name_font_name=self.name_font_name,
                                           icon_font_size=self.icon_font_size,
                                           name_font_size=self.name_font_size,
                                           on_event4=self.on_event4_pressed,
                                           on_event3=self.on_event3_pressed,
                                           on_event2=self.on_event2_pressed,
                                           on_event1=self.on_event1_pressed,
                                           on_press=self.on_menu_pressed,
                                           data=self.menu_data[i]))
            
    def on_menu_pressed(self,instance):
        self.data=instance.data
        self.item=instance
        self.dispatch("on_menu_selected")
    def on_menu_selected(self):
        pass
    def on_event4_pressed(self,instance):
        self.item=instance
        self.data=instance.data
        self.dispatch("on_event4_selected")
    def on_event3_pressed(self,instance):
        self.data=instance.data
        self.item=instance
        self.dispatch("on_event3_selected")
    def on_event2_pressed(self,instance):
        self.data=instance.data
        self.item=instance
        self.dispatch("on_event2_selected")
    def on_event1_pressed(self,instance):
        self.data=instance.data
        self.item=instance
        self.dispatch("on_event1_selected")
    
    def on_event4_selected(self):
        pass
    def on_event3_selected(self):
        pass
    def on_event2_selected(self):
        pass
    def on_event1_selected(self):
        pass
    

class GridMenuTextUnderIcon(GridMenu):
    menu_item=MenuItemTextUnderIcon
class GridMenuTextBesideIcon(GridMenu):
    menu_item=MenuItemTextBesideIcon
