#Variable admission

|Variable name | description | decision 
|:-------------|:------------|:---------
|graph_area | OUT, explained with other variables
|n | number of nodes in the graph | OUT, bigger cities have more
|m | number of edges in the graph | OUT, bigger cities have more
|k_avg | average node degree of the graph | IN (NB. bigger degree -> street network grid based, very low -> triangles)
|intersection_count | number of intersections in graph, that is, nodes with >1 street emanating from them | OUT, depends on the size
|streets_per_node_avg | how many streets (edges in the undirected representation of the graph) emanate from each node (ie, intersection or dead-end) on average (mean) | OUT?
|streets_per_node_counts | dict, with keys of number of streets emanating from the node, and values of number of nodes with this count | dict
|streets_per_node_proportion | dict, same as previous, but as a proportion of the total, rather than counts | dict
|edge_length_total | sum of all edge lengths in the graph, in meters | OUT, unscaled
|edge_length_avg | mean edge length in the graph, in meters | IN, includes edge length information, calculates twoway streets twice but that's okay
|street_length_total | sum of all edges in the undirected representation of the graph | OUT, unscaled
|street_length_avg | mean edge length in the undirected representation of the graph, in meters | OUT, measured with edge_length_avg)
|street_segments_count | number of edges in the undirected representation of the graph | OUT, but into variable telling ratio for one-way streets 
|node_density_km | n divided by area in square kilometers, multiple nodes in a street | OUT
|intersection_density_km | intersection_count divided by area in square kilometers | IN
|edge_density_km | edge_length_total divided by area in square kilometers | OUT expressed by street_density_km
|street_density_km | street_length_total divided by area in square kilometers | IN
|circuity_avg | edge_length_total divided by the sum of the great circle distances between the nodes of each edge, an area measurement of sorts | OUT
|self_loop_proportion | proportion of edges that have a single node as its two endpoints (ie, the edge links nodes u and v, and u||v), U-turn points | IN (NB. clearly visible in Ontario)
|clean_intersection_count | number of intersections in street network, merging complex ones into single points | left out
|clean_intersection_density_km | clean_intersection_count divided by area in square kilometers | left out
|avg_neighbor_degree || dict
|avg_neighbor_degree_avg || OUT tells similar story to k_avg 
|avg_weighted_neighbor_degree || dict
|avg_weighted_neighbor_degree_avg || OUT
|degree_centrality || dict
|degree_centrality_avg || IN, no betweenness
|clustering_coefficient || dict
|clustering_coefficient_avg || IN
|clustering_coefficient_weighted || dict
|clustering_coefficient_weighted_avg || weighing by n?, then OUT, because clusters are local and road network doesn't have infinitely long edges
|pagerank || dict
|pagerank_max_node | ID: OUT
|pagerank_max ||correlates strongly with n, should it be normalized?? What does it mean then? > normalize with n, IN
|pagerank_min_node || ID: OUT
|pagerank_min || OUT


New variable: percentage_twoway = (m - street_segments_count) / street_segments_count (percentage of twoway streets, NB. Barcelona, Valencia, Paris lowest)