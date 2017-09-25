+----------+-------------------+
| murder   | R Documentation   |
+----------+-------------------+

murder
------

Description
~~~~~~~~~~~

Data loads lazily. Type data(murder) into the console.

Usage
~~~~~

::

    data(murder)

Format
~~~~~~

A data.frame with 153 rows and 13 variables:

-  id. state identifier

-  state. postal code

-  year. 87, 90, or 93

-  mrdrte. murders per 100,000 people

-  exec. total executions, past 3 years

-  unem. annual unem. rate

-  d90. =1 if year == 90

-  d93. =1 if year == 93

-  cmrdrte. mrdrte - mrdrte[\_n-1]

-  cexec. exec - exec[\_n-1]

-  cunem. unem - unem[\_n-1]

-  cexec\_1. cexec[\_n-1]

-  cunem\_1. cunem[\_n-1]

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(murder)
