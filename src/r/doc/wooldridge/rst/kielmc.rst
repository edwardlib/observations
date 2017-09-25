+----------+-------------------+
| kielmc   | R Documentation   |
+----------+-------------------+

kielmc
------

Description
~~~~~~~~~~~

Data loads lazily. Type data(kielmc) into the console.

Usage
~~~~~

::

    data(kielmc)

Format
~~~~~~

A data.frame with 321 rows and 25 variables:

-  year. 1978 or 1981

-  age. age of house

-  agesq. age^2

-  nbh. neighborhood, 1-6

-  cbd. dist. to cent. bus. dstrct, ft.

-  intst. dist. to interstate, ft.

-  lintst. log(intst)

-  price. selling price

-  rooms. # rooms in house

-  area. square footage of house

-  land. square footage lot

-  baths. # bathrooms

-  dist. dist. from house to incin., ft.

-  ldist. log(dist)

-  wind. prc. time wind incin. to house

-  lprice. log(price)

-  y81. =1 if year == 1981

-  larea. log(area)

-  lland. log(land)

-  y81ldist. y81\*ldist

-  lintstsq. lintst^2

-  nearinc. =1 if dist <= 15840

-  y81nrinc. y81\*nearinc

-  rprice. price, 1978 dollars

-  lrprice. log(rprice)

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(kielmc)
