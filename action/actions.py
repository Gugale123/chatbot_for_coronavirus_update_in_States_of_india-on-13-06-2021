# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Thank you so much for using Rasa visit again ")

         return []
     


class Actionlocation(Action):

     def name(self) -> Text:
         return "action_update"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         data= pd.read_csv('https://api.covid19india.org/csv/latest/states.csv')
         data["Date"]=pd.to_datetime(data["Date"])
         entities=tracker.latest_message['entities']
         print(entities)
         for i in entities:
             i['entity']=='state'
             name=i['value']
         name=name.title()
         data["Date"]=pd.to_datetime(data["Date"])
         d=data[(data["State"]==str(name)) & (data["Date"]=='2021-06-13')]
         d=d.iloc[:,:].values
         st= "Date:"+str(d[0][0])+ " Confirmed:"+str(d[0][2])+" Recovered:"+str(d[0][3])+" Deceased:"+str(d[0][4])
         dispatcher.utter_message(text=st)
         
         return []
