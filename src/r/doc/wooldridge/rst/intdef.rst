+----------+-------------------+
| intdef   | R Documentation   |
+----------+-------------------+

intdef
------

Description
~~~~~~~~~~~

Data loads lazily. Type data(intdef) into the console.

Usage
~~~~~

::

    data(intdef)

Format
~~~~~~

A data.frame with 56 rows and 13 variables:

-  year. 1948 to 2003

-  i3. 3 month T-bill rate

-  inf. CPI inflation rate

-  rec. federal receipts, percent GDP

-  out. federal outlays, percent GDP

-  def. out - rec

-  i3\_1. i3[\_n-1]

-  inf\_1. inf[\_n-1]

-  def\_1. def[\_n-1]

-  ci3. i3 - i3\_1

-  cinf. inf - inf\_1

-  cdef. def - def\_1

-  y77. =1 if year >= 1977; change in FY

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(intdef)
