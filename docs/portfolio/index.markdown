---
layout: post
title:  "Portfolio"
permalink: /portfolio/
---

### 30 Day Mapping Challenge 2019

Mapping challenge to create a map every day in November.

![All 30 days.](https://gisforthought.com/media/2020-02-24_all_30.png)

[All maps.](https://gisforthought.com/portfolio/30-day-mapping-challenge-2019/)

[Read more.](https://gisforthought.com/30-day-map-challenge-2019/)

---

### Every Person in Great Britain Mapped

A follow up to the Scotland map. A point on the map for every person in Great Britain.

Generated using PostgreSQL/PostGIS, QGIS, with the web map in Leaflet JS.

<iframe src="https://maps.gisforthought.com/gb_population/index.html" width="100%" height="500"></iframe>
[Full screen.](https://maps.gisforthought.com/gb_population/index.html)
[Read more.](https://maps.gisforthought.com/gb_population/)

---

### UK Rail Map

Mapping the UK Rail network by agency and parent company. Collects data directly from the GTFS feed, automatically processes it every month using python and SQL, resulting in an up to date view of the UK rail network.

<img src="https://gisforthought.com/media/portfolio_UKRAIL_13643338343_810c69aff8_z.jpg" alt="network" height="400"/>
<img src="https://gisforthought.com/media/portfolio_UKRAIL_Capture1.PNG" alt="demo" height="400"/>

[Full page interactive map.](https://maps.gisforthought.com/uk_rail_map/)
[Read more.](https://gisforthought.com/uk-rail-map/)

---

### Every Person in Scotland Mapped

Winner of the 2016 [OS OpenData Award for Excellence in the use of OpenData](https://www.cartography.org.uk/awards/past-winners/2016-bcs-awards/) from the British Cartographic Society.

A point created for each person in Scotland, the points are placed inside of buildings that appear in postcodes. The count of points is determined by the population in each postcode.

Generated using PostgreSQL/PostGIS, QGIS, with the web map in Leaflet JS.

<iframe src="https://maps.gisforthought.com/cartography/index.html" width="100%" height="500"></iframe>
[Full screen.](https://maps.gisforthought.com/cartography/index.html)

---

### QGIS Multi Ring Buffer Plugin

Plugin to automate the creation of multiple buffer rings around a selection. Written in Python. Over 7000 downloads.

<img src="https://gisforthought.com/media/2018-02-07_CropperCapture76.png" alt="UI." width="300"/>
<img src="https://gisforthought.com/media/2018-02-07_CropperCapture77.png" alt="Action." width="300"/>

[QGIS Plugin Repository.](http://plugins.qgis.org/plugins/Multi_Ring_Buffer/)
[GitHub.](https://github.com/HeikkiVesanto/QGIS_Multi_Ring_Buffer)
[Read more.](https://gisforthought.com/qgis-multi-ring-buffer/)

---

### QGIS Centroid Within Selection Plugin

Plugin for QGIS to make centroid within and point on surface within selections. Written in Python. Over 2500 downloads.

<img src="https://gisforthought.com/media/2018-03-21_Select_within_GUI.png" alt="UI." width="300"/>
<img src="https://gisforthought.com/media/2018-03-21_Centroid-1024x656.png" alt="Action." width="400"/>

[QGIS Plugin Repository.](http://plugins.qgis.org/plugins/SelectWithin/)
[GitHub.](https://github.com/HeikkiVesanto/QGIS_Centroid_Within)
[Read more.](https://gisforthought.com/qgis-select-within-plugin/)

---

### UK Postcode Comparison

Accuracy comparison of UK postcode data generated from Ordnance Survey CodePoint Open. Postcode areas generated from centroids using voronoi polygons.

Open data generated postcodes were compared against postcode data released by the National Records for Scotland. Comparison done for actual area, and at a property level using the Glasgow Corporate Address Gazetteer.

![Postcode by source.](https://gisforthought.com/media/portfolio_postcode_glasgow_options.png)
<img src="https://gisforthought.com/media/portfolio_postcode.png" alt="Postcode breakdown" height="400"/>

[Read more part 1.](https://gisforthought.com/uk-postcode-polygon-accuracy-comparison/)

[Read more part 2.](https://gisforthought.com/uk-postcode-polygon-accuracy-comparison-part-2/)

---

### Great Circle Flight Lines

Generating great circle flight lines using PostgreSQL and PostGIS. Uses casting to geography to achieve the shortest geodesic route between any two points on the globe.

<img src="https://gisforthought.com/media/2014-11-26_15872020385_689541c6b0_o.png" alt="Great circle flight lines." height="400"/>
<img src="https://gisforthought.com/media/portfolio_helsinki-connections.png" alt="Helsinki flights." height="400"/>

[Read more.](https://gisforthought.com/great-circle-flight-lines-in-postgis/)

---

### Historic Outlines of Scotland

Mapping the historic outlines of Scotland between 1600-1700. Included georeferencing vector data using ogr2ogr.

<img src="https://gisforthought.com/media/2014-03-24_13352523035_0f80054b68_o.png" alt="Scotland Outline." height="600"/>

[Read more.](https://gisforthought.com/scotlands-changing-outline/)
