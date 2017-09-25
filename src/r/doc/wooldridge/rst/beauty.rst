+----------+-------------------+
| beauty   | R Documentation   |
+----------+-------------------+

beauty
------

Description
~~~~~~~~~~~

Data loads lazily. Type data(beauty) into the console.

Usage
~~~~~

::

    data(beauty)

Format
~~~~~~

A data.frame with 1260 rows and 17 variables:

-  wage. hourly wage

-  lwage. log(wage)

-  belavg. =1 if looks <= 2

-  abvavg. =1 if looks >=4

-  exper. years of workforce experience

-  looks. from 1 to 5

-  union. =1 if union member

-  goodhlth. =1 if good health

-  black. =1 if black

-  female. =1 if female

-  married. =1 if married

-  south. =1 if live in south

-  bigcity. =1 if live in big city

-  smllcity. =1 if live in small city

-  service. =1 if service industry

-  expersq. exper^2

-  educ. years of schooling

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(beauty)
