# Author: Riku Laine
# Date: Mon Feb 18 12:44:45 2019
# Project name: Network analysis
# Description : Script to clean and merge the network data with the statistics.

# Set working directory
setwd("C:/Users/Riku_L/network-analysis-uoh/data/")

# Read the data sets
inrix_data <- read.csv("scoreboard-traffic.csv", stringsAsFactors = F)

metrics <- read.csv2("inrix_cities_statistics.csv", stringsAsFactors = F)

# Remove escapes from city names
metrics$names <- gsub("[\"\n]", "", metrics$city_name)

# Merge
merged <- merge(inrix_data, metrics, by.x = "city_name", by.y = "names")

# Write to file. Separator is semicolon.
file_name <- "merged_traffic_network_statistics.csv"

if(!file.exists(file_name)){
	write.csv2(merged, file = file_name, row.names = F)
}
