##########
# Purpose: The script for retrieving OSMNX network data and calculating the
# basic metrics
# Author: Riku Laine
# Initiation date: 6 February, 2019
# Returns:
#   - Appends the dict of the statistics to a pickle file. The script creates it
#     if it doesn't exist.
#   - Writes / appends the statistics to a csv without the dicts.
##########

# Arguments to be provided: String, name of the geographical location. 

destination_pickle_file = "osmnx_statistics.pickle"
destination_csv_file = "osmnx_statistics.csv"

# Imports
import sys
import csv
import pickle
import os.path
import osmnx as ox
import warnings

#warnings.simplefilter('error', UserWarning)

# Create the place name, should define a geographical area, not a point.
place_name = " ".join(sys.argv[1:])

# Create networkx digraph
# NOTE! With these parameters, we obtain a simplified network of public streets. Refer to
# https://osmnx.readthedocs.io/en/stable/osmnx.html#osmnx.core.graph_from_place
# for more details. In the loop, first 15 query results are tried and if none
# of them resolve to Polygon, a warning is raised.

i = 1
while True:
    try:
        G = ox.graph_from_place(place_name, network_type='drive', 
                                retain_all=True, which_result = i)
        break
    except TypeError:
        i = i + 1

    if i > 15:
        raise UserWarning("The first 15 queries did not resolve to Polygons. ",
                          "Check location manually. Place: ", place_name)

    
# Calculate the area that the network covers in square meters.

G_proj = ox.project_graph(G)
nodes_proj = ox.graph_to_gdfs(G_proj, edges=False)
graph_area_m = nodes_proj.unary_union.convex_hull.area

# Calculate the basic and extended stats.

basic_stats = ox.basic_stats(G, area = graph_area_m)
ext_stats = ox.extended_stats(G, connectivity = True, anc = True, ecc = True,  bc = True, cc = True)

# Concatenate the statistics dictionaries and add city name and area to the
# beginning.
combined_stats = {"city_name" : place_name,
                  "graph_area" : graph_area_m,
                  **basic_stats,
                  **ext_stats}

# Load the dict from pickle and append.
if os.path.isfile(destination_pickle_file):
    with open(destination_pickle_file, 'rb') as f:
        to_pickle = {**pickle.load(f), place_name : combined_stats}
else:
    to_pickle = {place_name : combined_stats}

# Dump the dict in a pickle file.
with open(destination_pickle_file, "wb") as handle:
    pickle.dump(to_pickle, handle, protocol=pickle.HIGHEST_PROTOCOL)


# Loop the dict and remove the nested dicts for a cleaner csv.
for key in list(combined_stats.keys()):
    if type(combined_stats[key]) is dict:
        del combined_stats[key]

# Append the statistics to the files in semicolon separated format. Separator
# should be semicolon as the city names will contain commas. E.g place name
# could be "Helsinki, Finland". Writes header row if file does not exist.
csv_exists = os.path.isfile(destination_csv_file) 

with open(destination_csv_file, "a") as f:
    w = csv.DictWriter(f, combined_stats.keys(), delimiter=";")
    if not csv_exists:
        w.writeheader()
    w.writerow(combined_stats)


