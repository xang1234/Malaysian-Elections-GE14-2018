# Malaysian-Elections-GE14-2018

## Data

-  [Wikipedia Malaysian General Elections Results by Parliamentary Constituency](https://en.wikipedia.org/wiki/Results_of_the_Malaysian_general_election,_2018_by_parliamentary_constituency) *scraped on 30th August 2018*
-  [Malaysia Parliamentary Carto 2018](https://daneshtindak.carto.com/tables/malaysia_parliamentary_carto_2018/public) by Danesh Prakash Chacko from Tindak
-  [Malaysia Population Statistics](http://pqi.stats.gov.my) by the [Department of Statistics Malaysia](https://www.dosm.gov.my/v1/)

## R libraries
`geojsonio`, `tidyverse`, `leaflet`, `htmltools` , `shiny` , `plotly`, `flexdashboard`

## Application
*App is still a work in progress*

[View App Here](https://davidten.shinyapps.io/GE14dash/)

### Map tab
Tab displays:
- Electoral map with results of the 2018 General Elections
- Racial composition of voters in each parliamentary ward displayed when main map clicked
- Population pyramid of state in 2018 is displayed when main map is clicked

![Map Tab](/images/results.JPG?raw=true "Map Tab")

### Scatter plot tab
Tab displays bubble chart or ternary chart. User can select the axis, marker size and color.

![Scatter Tab](/images/bubble.JPG?raw=true "Scatter Tab")

![Scatter Tab](/images/ternary.JPG?raw=true "Scatter Tab")

### What If tab
User can project the number of seats in a 2 party parliamentary contest. Votes and turnout can be modified for each race. This simplistic model uses the same values for all seats and assumes that only 2 parties contest a seat. Projections are based on 2018 electoral composition. Bumiputera in Sabah and Sarawak are modelled as one block; in reality they are made up of multiple ethnicities. 

![What If](/images/what-if.JPG?raw=true "What If Tab")
