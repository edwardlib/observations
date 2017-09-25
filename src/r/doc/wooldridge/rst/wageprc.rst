+-----------+-------------------+
| wageprc   | R Documentation   |
+-----------+-------------------+

wageprc
-------

Description
~~~~~~~~~~~

Data loads lazily. Type data(wageprc) into the console.

Usage
~~~~~

::

    data(wageprc)

Format
~~~~~~

A data.frame with 286 rows and 20 variables:

-  price. consumer price index

-  wage. nominal hourly wage

-  t. time trend = 1, 2 , 3, ...

-  lprice. log(price)

-  lwage. log(wage)

-  gprice. lprice - lprice[\_n-1]

-  gwage. lwage - lwage[\_n-1]

-  gwage\_1. gwage[\_n-1]

-  gwage\_2. gwage[\_n-2]

-  gwage\_3.

-  gwage\_4.

-  gwage\_5.

-  gwage\_6.

-  gwage\_7.

-  gwage\_8.

-  gwage\_9.

-  gwage\_10.

-  gwage\_11.

-  gwage\_12.

-  gprice\_1. gprice[\_n-1]

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(wageprc)
