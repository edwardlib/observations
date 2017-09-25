+----------+-------------------+
| hseinv   | R Documentation   |
+----------+-------------------+

hseinv
------

Description
~~~~~~~~~~~

Data loads lazily. Type data(hseinv) into the console.

Usage
~~~~~

::

    data(hseinv)

Format
~~~~~~

A data.frame with 42 rows and 14 variables:

-  year. 1947-1988

-  inv. real housing inv, millions $

-  pop. population, 1000s

-  price. housing price index; 1982 = 1

-  linv. log(inv)

-  lpop. log(pop)

-  lprice. log(price)

-  t. time trend: t=1,...,42

-  invpc. per capita inv: inv/pop

-  linvpc. log(invpc)

-  lprice\_1. lprice[\_n-1]

-  linvpc\_1. linvpc[\_n-1]

-  gprice. lprice - lprice\_1

-  ginvpc. linvpc - linvpc\_1

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(hseinv)
