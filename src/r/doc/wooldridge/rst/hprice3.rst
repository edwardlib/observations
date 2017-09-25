+-----------+-------------------+
| hprice3   | R Documentation   |
+-----------+-------------------+

hprice3
-------

Description
~~~~~~~~~~~

Data loads lazily. Type data(hprice3) into the console.

Usage
~~~~~

::

    data(hprice3)

Format
~~~~~~

A data.frame with 321 rows and 19 variables:

-  year. 1978, 1981

-  age. age of house

-  agesq. age^2

-  nbh. neighborhood, 1-6

-  cbd. dist. to cent. bus. dstrct, ft.

-  inst. dist. to interstate, ft.

-  linst. log(inst)

-  price. selling price

-  rooms. # rooms in house

-  area. square footage of house

-  land. square footage lot

-  baths. # bathrooms

-  dist. dist. from house to incin., ft.

-  ldist. log(dist)

-  lprice. log(price)

-  y81. =1 if year = 1981

-  larea. log(area)

-  lland. log(land)

-  linstsq. linst^2

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(hprice3)
