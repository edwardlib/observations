+-----------+-------------------+
| airfare   | R Documentation   |
+-----------+-------------------+

airfare
-------

Description
~~~~~~~~~~~

Data loads lazily. Type data(airfare) into the console.

Usage
~~~~~

::

    data(airfare)

Format
~~~~~~

A data.frame with 4596 rows and 14 variables:

-  year. 1997, 1998, 1999, 2000

-  id. route identifier

-  dist. distance, in miles

-  passen. avg. passengers per day

-  fare. avg. one-way fare, $

-  bmktshr. fraction market, biggest carrier

-  ldist. log(distance)

-  y98. =1 if year == 1998

-  y99. =1 if year == 1999

-  y00. =1 if year == 2000

-  lfare. log(fare)

-  ldistsq. ldist^2

-  concen. = bmktshr

-  lpassen. log(passen)

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(airfare)
