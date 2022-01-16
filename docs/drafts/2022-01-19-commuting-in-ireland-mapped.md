---
layout: post
title:  "Commuting in Ireland Mapped"
---

As part of the 2016 Irish Census the Central Statistics Office captured data on communing to work and school/college ([POWSCAR](https://www.cso.ie/en/census/census2016reports/powscar/)). The raw data is available for research purposes, but the anonymised data is available to all. This data is aggregated to an Electoral Division (ED) level.

There are 3440 EDs in Ireland, 3409 after amalgamating low population ones. These are legally defined administrative areas. Commutes into Northern Ireland are also captured, but only as one destination (Northern Ireland).

Overall the data consists of a CSV file with 291893 rows of commuting data.

## Ireland

Mapping Irish commuting data at a country level allows us to see the patterns of commuting.

Maps inspired by [Dónal Casey](http://www.spatialoverlay.xyz/uncategorized/ireland-a-country-in-motion-1-96-million-commutes/).

![Purple](/assets/ireland-commuting/purp2.png)

The map styles can easily be achieved in [QGIS](https://www.qgis.org/). They utilise blending modes and variable levels of symbology based on the commuter counts.

A great guide can be found on this from the Ordnance Survey. [Carto tips: Using blend modes and opacity levels](https://www.ordnancesurvey.co.uk/newsroom/blog/carto-tips-using-blend-modes-opacity-levels)

I also talk about this at my FOSS4GUK 2019 talk: [YouTube - IE
FOSS4GUK LIVE - Main Room / Biosphere Green - DAY 2](https://www.youtube.com/watch?v=DlAfbwGrT30&t=5775s)

The purple map above use color: #6450d7 - Addition blend - 100% opacity - Line thickness: if ("count">1000, 1000, "count")/1000

Gold:

![Gold](/assets/ireland-commuting/gold.png)

Color:#e5b636 - Addition blend - 100% opacity

This map was featured in the [2020 GeoHipster calendar](https://geohipster.com/2020/03/).

Black and White:

![9 cities](/assets/ireland-commuting/Ireland_commuteBW.png)

Nine largest cities:

![9 cities](/assets/ireland-commuting/cities.png)

## Individual Cities

I have also created individual maps for all settlements in Ireland. This should give a better local picture of the commuter flows.

Settlements were linked to EDs based on a few characteristics:

- Settlement intersects ED AND either
- The original point on surface is within 100 meters of a settlement OR 
- 75% of the settlement is in the ED OR
- 90% of the ED is in the settlement

[List of all settlements.](https://gisforthought.com/projects/irish_commutes/)

Examples:

Donegal:

![Donegal](https://gisforthought.com/projects/irish_commutes/Donegal_Letterkenny.jpg)

Galway:

![Galway](https://gisforthought.com/projects/irish_commutes/Galway_Galway_city_and_suburbs.jpg)

Castleisland:

![Castleisland](https://gisforthought.com/projects/irish_commutes/Kerry_Castleisland.jpg)

Tramore:

![Tramore](https://gisforthought.com/projects/irish_commutes/Waterford_Tramore.jpg)