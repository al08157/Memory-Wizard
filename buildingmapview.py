from kivy_garden.mapview import MapView
from kivy.clock import Clock
from marketmarker import MarketMarker
import set
from kivy.uix.label import Label
from kivy.uix.popup import Popup

import sqlite3

class BuildingMapView(MapView):
    coordinate_set = set.coordinate_set
    
    getting_markets_timer=None
    market_names = []
    connection = None
    cursor = None
    
    

    def open_database_conncection(self):
        self.connection = sqlite3.connect('building.db')
        self.cursor = self.connection.cursor()


    def start_getting_markets_in_fov(self):
        #After one sec, get the markets in the field of view
        try:
            self.getting_markets_timer.cancel()
        except:
            pass
        self.getting_markets_timer=Clock.schedule_once(self.get_markets_in_fov,1)

        
    def get_markets_in_fov(self, *args):
        coordinate_set = list(self.coordinate_set)
        #get reference to main app and the database curson
        
        if not self.connection:
            self.open_database_conncection()


        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        sql_statement="Select * FROM building WHERE x > %s AND x < %s AND y > %s AND y < %s "%(min_lon, max_lon, min_lat, max_lat)
        self.cursor.execute(sql_statement)
        markets = self.cursor.fetchall()
        # print(markets)

        for market in markets:
            name = market[4]
            if name in self.market_names:
                continue
            else:
                self.add_market(market)
        for i in markets:
            name = i[4]
            lon = i[1]
            lat = i[2]
            for j  in coordinate_set:
                if lon == j[0] and lat == j[1]:
                    msg_box = Popup(title='Pending Task', content=Label(text=f'You have a task pending at {name}'), size_hint=(None, None), size=(500, 125), pos_hint={'x': 0.04, 'y': 0.85})
                    msg_box.open()

    def add_market(self, market):

        #Create the MarketMarker
        lat, lon = market[2], market[1]
        marker = MarketMarker(lat = lat, lon = lon )

        #Add the MarketMarker to the map
        self.add_widget(marker)



        # Keep trak of marker's name
        name = market[4]
        self.market_names.append(name) 
        marker.name = name
        marker.lat = lat
        marker.lon = lon

        
