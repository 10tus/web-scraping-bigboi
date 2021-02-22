from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.uix.screen import Screen
from kivymd.icon_definitions import md_icons
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from kivymd.uix.boxlayout import MDBoxLayout 
from stocktifyprocess import ProcessManager
from stocktifyprocess import SwipeStockItem
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.uix.label import MDLabel

        




            

class StocktifyApp(MDApp):
    listStock=[]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.ture=1
        
        
    
    def on_swipe_complete(self, instance):
        self.root.ids.md_list.remove_widget(instance)

    def on_start(self):
        #adds list of stock item if present in json
        pass
            
        
    

    def BackToMainScreen(self):
       self.root.ids.sc_manager.current="mainScreen"
       self.root.ids.s_code.text=""
       self.root.ids.res_price.text=""
       self.root.ids.sup_price.text=""

    
    def AcceptInput(self):
        #pm = Tester()
        #pm.WriteToJSON(pm.CreateJSON(self.root.ids.s_code.text,self.root.ids.res_price.text,self.root.ids.sup_price.text)) #save user input to json
        foc=SwipeStockItem(sCode=f'{self.root.ids.s_code.text}')
        self.listStock.append(foc)
        self.root.ids.md_list.add_widget(
            foc
        )
        Clock.schedule_interval(foc.Tick, 1)
        
    
    def TriggerNotify(self):        
        if self.root.ids.notif.icon == "bell":
            self.root.ids.notif.icon = "bell-off"        
        else: self.root.ids.notif.icon  = "bell"
        

    



StocktifyApp().run()
