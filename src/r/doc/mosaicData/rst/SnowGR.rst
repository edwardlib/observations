+----------+-------------------+
| SnowGR   | R Documentation   |
+----------+-------------------+

Snowfall data for Grand Rapids, MI
----------------------------------

Description
~~~~~~~~~~~

Official snowfall data by month and season for Grand Rapids, MI, going
back to 1893.

Usage
~~~~~

::

    data(SnowGR)

Format
~~~~~~

A data frame with 119 observations of the following variables.

-  ``SeasonStart`` Year in which season started (July is start of
   season)

-  ``SeasonEnd`` Year in which season ended (June is end of season)

-  ``Jul`` Inches of snow in July

-  ``Aug`` Inches of snow in August

-  ``Sep`` Inches of snow in September

-  ``Oct`` Inches of snow in October

-  ``Nov`` Inches of snow in November

-  ``Dec`` Inches of snow in December

-  ``Jan`` Inches of snow in January

-  ``Feb`` Inches of snow in February

-  ``Mar`` Inches of snow in March

-  ``Apr`` Inches of snow in April

-  ``May`` Inches of snow in May

-  ``Jun`` Inches of snow in June

-  ``Total`` Inches of snow for entire season (July-June)

Source
~~~~~~

These data were compiled by Laura Kapitula from data available at
http://www.crh.noaa.gov/grr/climate/data/grr/snowfall/.

Examples
~~~~~~~~

::

    data(SnowGR)
    if (require(mosaic)) {
      favstats(SnowGR$Total)
      histogram(~Total, data=SnowGR)
      xyplot(Total ~ SeasonStart, SnowGR, type=c('p','smooth'))
    }
    if (require(reshape2)) {
      Snow2 <- melt(SnowGR, id=1:2)
      names(Snow2)[3:4] <- c('Time','Snow')
      bwplot(Snow ~ Time, Snow2)
    }

