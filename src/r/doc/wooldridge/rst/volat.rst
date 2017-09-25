+---------+-------------------+
| volat   | R Documentation   |
+---------+-------------------+

volat
-----

Description
~~~~~~~~~~~

Data loads lazily. Type data(volat) into the console.

Usage
~~~~~

::

    data(volat)

Format
~~~~~~

A data.frame with 558 rows and 17 variables:

-  date. 1947.01 to 1993.06

-  sp500. S&P 500 index

-  divyld. div. yield annualized rate

-  i3. 3 mo. T-bill annualized rate

-  ip. index of industrial production

-  pcsp. pct chg, sp500, ann rate

-  rsp500. return on sp500: pcsp + divyld

-  pcip. pct chg, IP, ann rate

-  ci3. i3 - i3[\_n-1]

-  ci3\_1. ci3[\_n-1]

-  ci3\_2. ci3[\_n-2]

-  pcip\_1. pcip[\_n-1]

-  pcip\_2. pcip[\_n-2]

-  pcip\_3. pcip[\_n-3]

-  pcsp\_1. pcip[\_n-1]

-  pcsp\_2. pcip[\_n-2]

-  pcsp\_3. pcip[\_n-3]

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(volat)
