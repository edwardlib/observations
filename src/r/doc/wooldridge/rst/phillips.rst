+------------+-------------------+
| phillips   | R Documentation   |
+------------+-------------------+

phillips
--------

Description
~~~~~~~~~~~

Data loads lazily. Type data(phillips) into the console.

Usage
~~~~~

::

    data(phillips)

Format
~~~~~~

A data.frame with 56 rows and 7 variables:

-  year. 1948 through 2003

-  unem. civilian unemployment rate, percent

-  inf. percentage change in CPI

-  inf\_1. inf[\_n-1]

-  unem\_1. unem[\_n-1]

-  cinf. inf - inf\_1

-  cunem. unem - unem\_1

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(phillips)
