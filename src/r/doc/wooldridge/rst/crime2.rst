+----------+-------------------+
| crime2   | R Documentation   |
+----------+-------------------+

crime2
------

Description
~~~~~~~~~~~

Data loads lazily. Type data(crime2) into the console.

Usage
~~~~~

::

    data(crime2)

Format
~~~~~~

A data.frame with 92 rows and 34 variables:

-  pop. population

-  crimes. total number index crimes

-  unem. unemployment rate

-  officers. number police officers

-  pcinc. per capita income

-  west. =1 if city in west

-  nrtheast. =1 if city in NE

-  south. =1 if city in south

-  year. 82 or 87

-  area. land area, square miles

-  d87. =1 if year = 87

-  popden. people per sq mile

-  crmrte. crimes per 1000 people

-  offarea. officers per sq mile

-  lawexpc. law enforce. expend. pc, $

-  polpc. police per 1000 people

-  lpop. log(pop)

-  loffic. log(officers)

-  lpcinc. log(pcinc)

-  llawexpc. log(lawexpc)

-  lpopden. log(popden)

-  lcrimes. log(crimes)

-  larea. log(area)

-  lcrmrte. log(crmrte)

-  clcrimes. change in lcrimes

-  clpop. change in lpop

-  clcrmrte. change in lcrmrte

-  lpolpc. log(polpc)

-  clpolpc. change in lpolpc

-  cllawexp. change in llawexp

-  cunem. change in unem

-  clpopden. change in lpopden

-  lcrmrt\_1. lcrmrte lagged

-  ccrmrte. change in crmrte

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(crime2)
