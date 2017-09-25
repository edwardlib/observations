+---------+-------------------+
| earns   | R Documentation   |
+---------+-------------------+

earns
-----

Description
~~~~~~~~~~~

Data loads lazily. Type data(earns) into the console.

Usage
~~~~~

::

    data(earns)

Format
~~~~~~

A data.frame with 41 rows and 14 variables:

-  year. 1947 to 1987

-  wkearns. avg. real weekly earnings

-  wkhours. avg. weekly hours

-  outphr. output per labor hour

-  hrwage. wkearns/wkhours

-  lhrwage. log(hrwage)

-  loutphr. log(outphr)

-  t. time trend: t=1 to 47

-  ghrwage. lhrwage - lhrwage[\_n-1]

-  goutphr. loutphr - loutphr[\_n-1]

-  ghrwge\_1. ghrwage[\_n-1]

-  goutph\_1. goutphr[\_n-1]

-  goutph\_2. goutphr[\_n-2]

-  lwkhours. log(wkhours)

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(earns)
