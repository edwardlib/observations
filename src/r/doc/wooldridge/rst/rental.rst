+----------+-------------------+
| rental   | R Documentation   |
+----------+-------------------+

rental
------

Description
~~~~~~~~~~~

Data loads lazily. Type data(rental) into the console.

Usage
~~~~~

::

    data(rental)

Format
~~~~~~

A data.frame with 128 rows and 23 variables:

-  city. city label, 1 to 64

-  year. 80 or 90

-  pop. city population

-  enroll. # college students enrolled

-  rent. average rent

-  rnthsg. renter occupied units

-  tothsg. occupied housing units

-  avginc. per capita income

-  lenroll. log(enroll)

-  lpop. log(pop)

-  lrent. log(rent)

-  ltothsg. log(tothsg)

-  lrnthsg. log(rnthsg)

-  lavginc. log(avginc)

-  clenroll. change in lrent from 80 to 90

-  clpop. change in lpop

-  clrent. change in lrent

-  cltothsg. change in ltothsg

-  clrnthsg. change in lrnthsg

-  clavginc. change in lavginc

-  pctstu. percent of population students

-  cpctstu. change in pctstu

-  y90. =1 if year == 90

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(rental)
