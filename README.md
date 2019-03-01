# City street analysis from a network and topology perspective

This repository is for network analysis [course](https://courses.helsinki.fi/fi/data16001/) in University of Helsinki.

## Research questions

### Street network classification
We were interested in whether it is possible to classify city networks based on network properties. We used e.g. the OSMnx library for obtaining the street network metrics for different cities in INRIX 2018 [scorecard](http://inrix.com/scorecard/).

### Hotspot prediction
In addition we tried to predict some traffic delay hotspot as specified by TomTom in their website. We used e.g. PageRank, betweenness and degree centrality.

### Statistical inference
A log-linear model was built to infer the network measures affecting the travel time and speed.

## About the repository

*Structure:*

* `Data` file contains the data files obtained with the scripts and pictures.
* `Scripts` file contains the Python and bash script used to retrieve the data with the library and slurm. It also contains some Jupter notebooks used in different analysis and visualisations.
