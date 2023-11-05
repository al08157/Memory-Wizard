from kivy.app import App
from kivy_garden.mapview import MapMarkerPopup
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class MarketMarker(MapMarkerPopup):
    def on_release(self):
        #Open up the LocationPopupMenu
        popup = Popup(title='Location:', content=Label(text=self.name), size_hint=(None, None), size=(200, 100))
        
        def print_location(*args):
            # Get a reference to the app
            app = App.get_running_app()

            # Remove the last location in the selected_locations list
            if app.selected_locations:
                app.selected_locations.pop()
            
            # Add the new location to the selected_locations list
            app.selected_locations.append({"lon": self.lon, "lat": self.lat})

            # Print the location information
            print(f"Name: {self.name}\nLat: {self.lat}\nLon: {self.lon}")
            

        popup.bind(on_open=print_location)
        popup.open()