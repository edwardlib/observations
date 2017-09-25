+----------+-------------------+
| crime3   | R Documentation   |
+----------+-------------------+

crime3
------

Description
~~~~~~~~~~~

Data loads lazily. Type data(crime3) into the console.

Usage
~~~~~

::

    data(crime3)

Format
~~~~~~

A data.frame with 106 rows and 12 variables:

-  district. district number

-  year. 72 or 78

-  crime. crimes per 1000 people

-  clrprc1. clear-up perc, prior year

-  clrprc2. clear-up perc, two-years prior

-  d78. =1 if year = 78

-  avgclr. (clrprc1 + clrprc2)/2

-  lcrime. log(crime)

-  clcrime. change in lcrime

-  cavgclr. change in avgclr

-  cclrprc1. change in clrprc1

-  cclrprc2. change in clrprc2

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(crime3)
