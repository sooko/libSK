from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config
Config.set("graphics","height","900")
Config.set("graphics","width","900")
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 1300)
Config.set('graphics', 'top', 400)
from kivy.uix.floatlayout import FloatLayout
import os
import sys
import hashlib
from kivy.clock import Clock
from kivy.lang.builder import Builder
Builder.unload_file("t.kv")
Builder.load_file("t.kv")

def md5_checksum_directory(directory):
    md5_hash = hashlib.md5()
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            with open(filepath, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    md5_hash.update(byte_block)
    return md5_hash.hexdigest()



class Ml(FloatLayout):
    md5=""
    contain_module="libsk"
    project_dir="libsk"
    list_sys=[]
    def __init__(self, **kwargs):
        super(Ml,self).__init__(**kwargs)
        self.initial_modules = set(sys.modules.keys())
        Clock.schedule_interval(self.timer,.5)
    def timer(self,dt):
        md5_dir= md5_checksum_directory(self.project_dir)
        if self.md5 != md5_dir:
            self.md5=md5_dir
            for i in sys.modules:
                # print(i)
                # if 
                if self.contain_module in i:
                    # print(i)
                    self.list_sys.append(i)
                    # del sys.modules[i]
            for i in self.list_sys:
                if i in sys.modules:
                    del sys.modules[i]
                
            # for module in set(sys.modules) :#- self.initial_modules:
            #     print(module)
                # if self.contain_module in module:
                #     del sys.modules[module]
                    
            Clock.schedule_once(self.delay,.5)
    def delay(self,dt):
        
        try:
            from libsk import LibSK
            
            self.container.clear_widgets()
            self.container.add_widget(LibSK())
        except Exception as e:
            print(e)
            
            

class TestApp(App):
    def build(self):
        return Ml()

if __name__ == '__main__':
    TestApp().run()

