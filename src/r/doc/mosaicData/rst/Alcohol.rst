+-----------+-------------------+
| Alcohol   | R Documentation   |
+-----------+-------------------+

Alcohol Consumption per Capita
------------------------------

Description
~~~~~~~~~~~

These data provide per capita alcohol consumption values for many
countries in 2005 and 2008. There are also a few countries for which
there are data in other years.

Usage
~~~~~

::

    data(Alcohol)

Format
~~~~~~

A data frame with 411 observations on the following variables.

-  ``country`` country name

-  ``year`` year

-  ``alcohol`` per capita alcohol consumption

Source
~~~~~~

Gapminder (http://www.gapminder.org/)

References
~~~~~~~~~~

http://www.fvgreenway.org/pdfs/Northampton-Bikepath-Volume-Counts

Examples
~~~~~~~~

::

    data(Alcohol)
    # There are only a few observations in years other than 2005 and 2008
    subset(Alcohol, ! year %in% c(2005,2008))
