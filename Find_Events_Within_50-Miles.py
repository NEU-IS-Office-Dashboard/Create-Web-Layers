#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#connect to GIS
import os
from arcgis.gis import GIS
gis = GIS("Home") # You may use "Home" or will need to replace this with ("http://www.arcgis.com", "YOUR USERNAME", "YOUR PASSWORD") to link the outputs to you account

# If a layer for summaries of events within 50-miles exists, delete it
feature_search = gis.content.search(query = 'EventsWithin50MilesNEU', item_type = "Feature Layer Collection")
if len(feature_search) > 0:
    for item in feature_search:
        item.delete()
        print("Deleted existing " + str(item) + " Feature Layer Collection")


# In[ ]:


# Access relevant data layers
# 50-Mile Buffer (do not replace this ID without an appropriate alternative, it provides the area within which to search for incidents):
buffers = gis.content.get("23e2b55bb99d4cd788034d0a4033c4df")
buffers1 = buffers.layers[0]

# To use this tool with other layers, all you need are the ArcGIS Online IDs from each.
# Replace the IDs in the quoutes with others to change items.
item1 = gis.content.get("9e2f2b544c954fda9cd13b7f3e6eebce") #currently: Recent Earthquakes by Magnitude
item1Layer = item1.layers[0]

item2 = gis.content.get("d957997ccee7408287a963600a77f61f") #currently: U.S. Current Wildfire Perimeters
item2Layer = item2.layers[0]


# In[ ]:


# Access the geoanalytics summarize data analysis module
from arcgis.features import summarize_data

# Join Item 1 (earthquakes) to buffers
item1_50Miles = summarize_data.join_features(buffers1, item1Layer, 'Intersects')
item1_50Miles


# In[ ]:


# Join Item 2 to Item 1 + buffers
events50Miles = summarize_data.join_features(item1_50Miles, item2Layer, 'Intersects', output_name="EventsWithin50MilesNEU")
events50Miles


# In[ ]:




