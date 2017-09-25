+-----------+-------------------+
| fertil3   | R Documentation   |
+-----------+-------------------+

fertil3
-------

Description
~~~~~~~~~~~

Data loads lazily. Type data(fertil3) into the console.

Usage
~~~~~

::

    data(fertil3)

Format
~~~~~~

A data.frame with 72 rows and 24 variables:

-  gfr. births per 1000 women 15-44

-  pe. real value pers. exemption, $

-  year. 1913 to 1984

-  t. time trend, t=1,...,72

-  tsq. t^2

-  pe\_1. pe[\_n-1]

-  pe\_2. pe[\_n-2]

-  pe\_3. pe[\_n-3]

-  pe\_4. pe[\_n-4]

-  pill. =1 if year >= 1963

-  ww2. =1, 1941 to 1945

-  tcu. t^3

-  cgfr. change in gfr: gfr - gfr\_1

-  cpe. pe - pe\_1

-  cpe\_1. cpe[\_n-1]

-  cpe\_2. cpe[\_n-2]

-  cpe\_3. cpe[\_n-3]

-  cpe\_4. cpe[\_n-4]

-  gfr\_1. gfr[\_n-1]

-  cgfr\_1. cgfr[\_n-1]

-  cgfr\_2. cgfr[\_n-2]

-  cgfr\_3. cgfr[\_n-3]

-  cgfr\_4. cgfr[\_n-4]

-  gfr\_2. gfr[\_n-2]

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(fertil3)
