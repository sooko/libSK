from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
from kivy.properties import NumericProperty,ListProperty,ColorProperty
from kivy.metrics import dp
Builder.load_string("""
<SKChartPlot>:
    canvas:
        Color:
            rgba:root.plot_color
        Line:
            points:root.line_points
            width:root.line_width
            
<SKChartLabelY>:
    halign:"left"
    valign:"middle"
    text_size:self.size
<SKChartGridY>:
    canvas:
        Color:
            rgba:root.color
        Line:
            points:[self.x,self.y,self.right,self.y]
<SKChartGridX>:
    canvas:
        Color:
            rgba:root.color
        Line:
            points:[self.x,self.y,self.x,self.top]
<VerticalSpacer@Widget>:
    size_hint:1,None
<HorizonSpacer@Widget>:
    size_hint:None,1

<RootLabelY>:
    y_translate:1  #self.height/root.major_y/2
    orientation:"vertical"
    id:root_label_y 
    canvas.before:
        PushMatrix:
        Translate:
            y:root.y_translate
    canvas.after:
        PopMatrix
<RootLabelX>:
    size_hint: 1, None
    canvas.before:
        PushMatrix:
        Translate:
            x:root.x_translate#self.width/root.major_x/2
    canvas.after:
        PopMatrix
<ChartBorder>:
    pos_hint: {'center_x': 0.5,'center_y': 0.5}
    canvas:
        Color:
            rgba:root.border_top_color
        Line:
            points:self.x,self.top,self.right,self.top
        Color:
            rgba:root.border_bottom_color
        Line:
            points:self.x,self.y,self.right,self.y
        Color:
            rgba:root.border_left_color
        Line:
            points:self.x,self.y,self.x,self.top
        Color:
            rgba:root.border_right_color
        Line:
            points:self.right,self.y,self.right,self.top
<RootMinValueLabel>:
    size_hint: 1, None
    SKChartLabelY:  
        pos_hint: {'center_x': 0.5,'center_y': 0.5}
        color:root.label_y_color
        font_size:root.label_font_size
        text:"{}".format(root.min_y_value)
        canvas.before:
            PushMatrix:
            Translate:
                y:root.y_translate#self.height/2
        canvas.after:
            PopMatrix
    Label:
        pos_hint: {'center_x': 0.5,'center_y': 0.5}
        color:root.label_x_color
        font_size:root.label_font_size
        text:"{}".format(root.min_x_value)
        canvas.before:
            PushMatrix:
            Translate:
                x:root.x_translate#self.width/2
        canvas.after:
            PopMatrix
    
<SKChart>:
    pos_hint: {'center_x': 0.5,'center_y': 0.5}
    BoxLayout:
        pos_hint: {'center_x': 0.5,'center_y': 0.5}
        orientation:"vertical"
        VerticalSpacer:
            height:root.vertical_spacer_height
        BoxLayout:
            pos_hint: {'center_x': 0.5,'center_y': 0.5}
            BoxLayout:
                orientation: 'vertical'
                size_hint: None, 1 
                width: root.label_y_width
                RootLabelY:
                    id:root_label_y
                    y_translate:self.height/root.major_y/2
                RootMinValueLabel:
                    height: root.label_x_height
                    label_y_color   :root.label_y_color   
                    label_x_color   :root.label_x_color   
                    label_font_size :root.label_font_size
                    y_translate     :self.height/2
                    x_translate     :self.width/2
                    min_x_value     :root.min_x_value
                    min_y_value     :root.min_y_value
                    
                    
            BoxLayout:
                orientation: 'vertical'
                FloatLayout:
                    id:root_plot_area
                    ChartBorder:
                        border_top_color   :root.border_top_color       
                        border_left_color  :root.border_left_color  
                        border_right_color :root.border_right_color 
                        border_bottom_color:root.border_bottom_color
                    BoxLayout:
                        pos_hint: {'center_x': 0.5,'center_y': 0.5}
                        id:root_grid_y
                        orientation:"vertical"
                    BoxLayout:
                        pos_hint: {'center_x': 0.5,'center_y': 0.5}
                        id:root_grid_x
                    Widget:
                        id:plot_area
                        pos_hint: {'center_x': 0.5,'center_y': 0.5}
                RootLabelX:
                    size_hint: 1, None
                    height: root.label_x_height   
                    id:root_label_x
                    x_translate:self.width/root.major_x/2
            HorizonSpacer:
                width:root.horizon_spacer_width
                


""")
                    
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
class SKChartGridX(Widget):
    color=ListProperty([1,1,1,1])


class SKChartGridY(Widget):
    color=ListProperty([1,1,1,1])

class SKChartLabelX(Label):
    pass


class SKChartLabelY(Label):
    pass
class RootLabelY(BoxLayout):
    y_translate=NumericProperty(0)
    # pass
class RootLabelX(BoxLayout):
    x_translate=NumericProperty(0)
    # pass

class RootMinValueLabel(FloatLayout):
    # pass
    label_y_color   =ListProperty([1,1,1,1])
    label_x_color   =ListProperty([1,1,1,1])
    label_font_size =NumericProperty(14)
    y_translate     =NumericProperty(0)
    x_translate     =NumericProperty(0)
    min_x_value     =NumericProperty(0)
    min_y_value     =NumericProperty(0)
    

class SKChartPlot(Widget):
    max=NumericProperty(100)
    min=NumericProperty(0)
    value=NumericProperty(0)
    plot_color=ColorProperty([1,1,1,1])
    line_points=ListProperty([])
    line_width=NumericProperty(dp(1))
    def __init__(self, **kwargs):
        super(SKChartPlot,self).__init__(**kwargs)

    
class ChartBorder(Widget):
    border_color       =ListProperty([1,1,1,1])
    border_left_color  =ListProperty([1,1,1,1])
    border_right_color =ListProperty([1,1,1,1])
    border_bottom_color=ListProperty([1,1,1,1])
    border_top_color=ListProperty([1,1,1,1])


class SKChart(FloatLayout):
    label_x_height   = NumericProperty(dp(40))
    label_y_width   = NumericProperty(dp(40))
    label_font_size = NumericProperty(dp(12))
    major_x         = NumericProperty(10)
    major_y         = NumericProperty(8)
    max_y_value     = NumericProperty(15)
    min_y_value     = NumericProperty(11)
    max_x_value     = NumericProperty(10)
    min_x_value     = NumericProperty(0)
    border_color       =ListProperty([1,1,1,1])
    border_left_color  =ListProperty([1,1,1,1])
    border_right_color =ListProperty([1,1,1,1])
    border_bottom_color=ListProperty([1,1,1,1])
    border_top_color=ListProperty([1,1,1,1])
    grid_x_color    =ListProperty([1,1,1,1])
    grid_y_color    =ListProperty([1,1,1,1])
    label_x_color    =ListProperty([1,1,1,1])
    label_y_color    =ListProperty([1,1,1,1])
    horizon_spacer_width  =NumericProperty(20)
    vertical_spacer_height=NumericProperty(20)    
    

    def __init__(self, **kwargs):
        super(SKChart,self).__init__(**kwargs)
        Clock.schedule_once(self.create,.2)
    def format_float(self,num):
        if num.is_integer():
            return int(num)
        else:
            return num
    def create(self,dt):
        self.ids.root_grid_y.clear_widgets()
        self.ids.root_label_y.clear_widgets()
        self.ids.root_grid_x.clear_widgets()
        self.ids.root_label_x.clear_widgets()
        step_y=(self.max_y_value-self.min_y_value)/self.major_y
        step_x=(self.max_x_value-self.min_x_value)/self.major_x
        for i in range(self.major_y):
            y_label=self.format_float(self.max_y_value-i*step_y)
            str_label_y="{}".format(y_label)
            self.ids.root_grid_y.add_widget(SKChartGridY(color=self.grid_y_color))
            self.ids.root_label_y.add_widget(SKChartLabelY(color=self.label_y_color,font_size=self.label_font_size,text=str_label_y))
        for i in range(self.major_x):
            self.ids.root_grid_x.add_widget(SKChartGridX(color=self.grid_x_color))
            x_label=self.min_x_value+step_x+i*step_x
            self.ids.root_label_x.add_widget(SKChartLabelX(color=self.label_x_color,font_size=self.label_font_size,text=str(self.format_float(x_label))))
    
    


        

