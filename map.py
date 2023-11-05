import requests
from kivy.app import App
from kivy.lang import Builder
from kivy_garden.mapview import MapView, MapMarkerPopup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty

# Set the Kivy window size
from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')

# Load the KV file for the layout
Builder.load_string("""
<RootWidget>:
    orientation: "vertical"
    search_bar: search_bar
    search_button: search_button
    mapview: mapview

    BoxLayout:
        size_hint_y: None
        height: 40
        TextInput:
            id: search_bar
            size_hint_x: 0.8
            text: root.search_text
            multiline : False
            on_text_validate: root.search_on_map()
        Button: 
            id: search_button
            size_hint_x: 0.2
            text: "Search"
            on_release: root.search_on_map()

    MapView:
        id: mapview
        lat: 24.8607
        lon: 67.0011
        zoom: 11
""")


# Define the main app class
class RootWidget(BoxLayout):
    search_text = StringProperty("Sukkur, Sindh, Pakistan")

    def search_on_map(self):
        search_query = self.search_bar.text
        print(f'Search query: {search_query}')
        api_key = "AIzaSyBh41aJgTxo_zX5mg6NGO39HGFD0xP_t5Q"
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={search_query}&key={api_key}"
        response = requests.get(url)
        response_json = response.json()
        if response_json["status"] == "OK":
            location = response_json["results"][0]["geometry"]["location"]
            self.mapview.center_on(location["lat"], location["lng"])

            # Remove all existing markers
            for child in self.mapview.children[:]:
                if type(child) == MapMarkerPopup:
                    self.mapview.remove_marker(child)

            # Add a new marker for the search location
            marker = MapMarkerPopup(lat=self.mapview.lat, lon=self.mapview.lon, source='marker.png', size=(50,50))
            self.mapview.add_marker(marker)

    def on_search_text(self, instance, value):
        self.search_bar.text = value


# Define the app class
class MapApp(App):
    def build(self):
        return RootWidget()


# Run the app
if __name__ == '__main__':
    MapApp().run()
