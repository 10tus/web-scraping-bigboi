from bs4 import BeautifulSoup
import requests
import time
import json
import os.path
import concurrent.futures
from kivymd.uix.card import MDCardSwipe
from kivy.properties import StringProperty
from kivymd.utils import asynckivy

#make this asynchronous
class SwipeStockItem(MDCardSwipe):
    sCode=StringProperty()
    
    def Tick(self,*args):
        async def Update():
            req = requests.get("https://www.investagrams.com/Stock/PSE:"+self.sCode)
            s=BeautifulSoup(req.text,"lxml")
            lp=s.find('span',{'id':'lblStockLatestLastPrice'}).text
            self.ids.curr_price.text=f'{lp}'
        asynckivy.start(Update()) 


class ProcessManager():
    stocksList=[]
        
    def WriteToJSON(self,data,file='data.json'):
        with open(file,'w') as f: 
            json.dump(data, f, indent=4)
    
    """
    def Tick(self):
        with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
            executor.map(self.AnalyzeInput,self.stocksList)"""


    def ReadJSON(self):
        return 0

    def CreateJSON(self,sCard,resPrice,supPrice,file="data.json"):
        data=''
        if not(os.path.exists(file)): #checks if data.json is not yet created
            data = {"stock":[{sCard:{
                            "resist":resPrice,
                            "support":supPrice
                        }
                    }
                ]
            }
            
        else:
            with open('data.json') as json_file: 
                data = json.load(json_file) 
                
                temp = data['stock'] 
            
                # python object to be appended 
                obj = {sCard:{
                            "resist":resPrice,
                            "support":supPrice
                        }
                    }
            
            
                # appending data to emp_details  
                temp.append(obj)
        self.stocksList.append(sCard)
        return data
          



