title: Plotting Hotspots in Mauritius with Python and Folium
slug: plotting-hotspots-in-mauritius-with-python-and-folium
pub: Wed, 23 Jan 2019 08:01:11 +0000


geo plotting has never been so easy. thanks dhrumil patel!




download the data file [here](https://data.govmu.org/dkan/?q=dataset/350-wifi-hotspots-mauritius-2017)





```python

#Import Library
import folium
import pandas as pd

#Load Data
data = pd.read_csv("hotspot.csv")
lat = data['Longitude']
lon = data['Latitude']
elevation = data['Location']

#Create base map
map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 5, tiles = "Mapbox bright")

#Plot Markers
for lat, lon, elevation in zip(lat, lon, elevation):
    folium.Marker(location=[lat, lon], popup=str(elevation), icon=folium.Icon(color = 'gray')).add_to(map)

#Save the map
map.save("hostspots.html")

```





