+------------+-------------------+
| Births78   | R Documentation   |
+------------+-------------------+

US Births in 1978
-----------------

Description
~~~~~~~~~~~

A day by day record of the number of births in the United States in
1978.

Usage
~~~~~

::

    data(Births78)

Format
~~~~~~

A data frame with 365 observations on the following variables.

-  ``date`` date in 1978

-  ``births`` number of US births

-  ``dayofyear`` sequential number of days from 1 to 365

-  ``wday`` day of week as an ordered factor

Examples
~~~~~~~~

::

    data(Births78)
    if (require(lattice)) {
      xyplot(births ~ date, Births78)
      xyplot(births ~ date, Births78, groups = wday)
    }
