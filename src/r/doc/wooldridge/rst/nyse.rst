+--------+-------------------+
| nyse   | R Documentation   |
+--------+-------------------+

nyse
----

Description
~~~~~~~~~~~

Data loads lazily. Type data(nyse) into the console.

Usage
~~~~~

::

    data(nyse)

Format
~~~~~~

A data.frame with 691 rows and 8 variables:

-  price. NYSE stock price index

-  return. 100\*(p - p(-1))/p(-1))

-  return\_1. lagged return

-  t.

-  price\_1.

-  price\_2.

-  cprice. price - price\_1

-  cprice\_1. lagged cprice

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(nyse)
