##########
# Purpose: The script for retrieving OSMNX network data and calculating the
# basic metrics
# Author: Riku Laine
# Initiation date: 6 February, 2019
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

# Create the place name, should define a geographical area, not a point.
place_name = " ".join(sys.argv[1:])

# Create networkx digraph
# NOTE! With these parameters, we obtain a simplified network of public streets. Refer to
# https://osmnx.readthedocs.io/en/stable/osmnx.html#osmnx.core.graph_from_place
# for more details.

G = ox.graph_from_place(place_name, network_type='drive', retain_all=True)

# Calculate the area that the network covers in square meters.

G_proj = ox.project_graph(G)
nodes_proj = ox.graph_to_gdfs(G_proj, edges=False)
graph_area_m = nodes_proj.unary_union.convex_hull.area

# Calculate the basic and extended stats.

basic_stats = ox.basic_stats(G, area = graph_area_m)
ext_stats = ox.extended_stats(G)

# Concatenate the statistics dictionaries and add city name and area to the
# beginning.
combined_stats = {"city_name" : place_name,
                  "graph_area" : graph_area_m,
                  **basic_stats,
                  **ext_stats}

# Dump the dict in a pickle file by appending.
with open(destination_pickle_file, "ab") as handle:
    pickle.dump(combined_stats, handle, protocol=pickle.HIGHEST_PROTOCOL)


# Loop the dict and remove the nested dicts:
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


