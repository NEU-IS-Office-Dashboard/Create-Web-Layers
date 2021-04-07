# created by: Alex Clippinger
# e-mail: clippinger.a@northeastern.edu
# date: 2021-04-06

# the following script produces a summary file for the web layers of the ArcGIS Dashboard
# for the NEU IS office.
# execute the script to output an excel file to your working directory.

# import arcgis libraries and modules
import arcgis
from arcgis import GIS
from arcgis.mapping import WebMap

# initiate connection to ArcGIS Online
gis = GIS("Home")

# access web map used in the dashboard
web_map = gis.content.get('e52b2e79cf304c128aa0d9a61cf5077b')\

# create WebMap object
web_map = WebMap(web_map)

# get columns of layer names, ids, and layer types

# create empty lists 
col1 = []
col2 = []
col3 = []

# iterate through layers in web map
for layer in web_map.layers:
    
    #append titles, ids, and layer types to fill empty lists
    col1.append(layer.title)
    col2.append(layer.itemId)
    col3.append(layer.layerType)

# get columns of Layer information (exists, status, owner, links)

# create empty lists
col4 = []
col5 = []
col6 = []
col7 = []

# iterate through itemIds from column 2 above
for uid in col2:
    
    # check if itemid returns a result. 
    if len(gis.content.search(uid, outside_org = True)) > 0:
        
        # if the itemid returns any result, then it exists
        col4.append('Yes')
        
        # if itemid returns any result, then fetch the layer
        layer = gis.content.get(str(uid))
        
        # use the layer information to append owner and link to fill empty lists
        col6.append(layer.owner)
        col7.append(layer.homepage)
        
        # for layers that exist, check the layer status and append to fill empty list
        if layer.content_status == 'deprecated':
            col5.append('Layer has been deprecated')
        else:
            col5.append('Active')
    
    # return if the itemid does not return any result.
    else:
        col4.append('Layer does not exist.')

# import pandas to work with dataframes
import pandas as pd

# create columns
d = {'Layer Title': col1, 
     'Layer ID': col2, 
     'Layer Type': col3, 
     'Layer Exists': col4, 
     'Layer Status': col5,
     'Owner': col6,
     'Link': col7}

# create dataframe
df = pd.DataFrame(d)

# import datetime module
from datetime import datetime

# get today's date for file name
date = datetime.today().strftime('%Y-%m-%d')

# import the os module
import os

# create file path
path = os.path.join('Dashboard_Layers-Summary_' + date + '.xlsx')

# save dataframe to an excel file
df.to_excel(path,
            sheet_name = str(date))

# Note: this will be saved to your working directory. 
# To check your working directory, use the code below:
# > import os
# > os.getcwd()
# To change your working directory, use the code below:
# > import os
# > os.chdir('new/file/path/here')
