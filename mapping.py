from kivy.app import App
from kivy.garden.mapview import MapView, MapMarkerPopup
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class MapViewApp(App):
    
    def build(self):
        # Set up the map view
        mapview = MapView(zoom=11, lat=24.8607, lon=67.0011) # center map on Karachi
        marker = MapMarkerPopup(lat=24.8607, lon=67.0011, source='marker.png', size_hint=(None,None),width = 0.1, height = 0.1)
        mapview.add_marker(marker)

        # Set up the layout
        layout = FloatLayout()
        layout.add_widget(mapview)
        btn = Button(text='Hello Karachi!', size_hint=(0.2,0.1), pos_hint={'x':0.4,'y':0})
        layout.add_widget(btn)

        return layout

if __name__ == '__main__':
    MapViewApp().run()