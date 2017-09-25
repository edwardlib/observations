+----------+-------------------+
| jtrain   | R Documentation   |
+----------+-------------------+

jtrain
------

Description
~~~~~~~~~~~

Data loads lazily. Type data(jtrain) into the console.

Usage
~~~~~

::

    data(jtrain)

Format
~~~~~~

A data.frame with 471 rows and 30 variables:

-  year. 1987, 1988, or 1989

-  fcode. firm code number

-  employ. # employees at plant

-  sales. annual sales, $

-  avgsal. average employee salary

-  scrap. scrap rate (per 100 items)

-  rework. rework rate (per 100 items)

-  tothrs. total hours training

-  union. =1 if unionized

-  grant. = 1 if received grant

-  d89. = 1 if year = 1989

-  d88. = 1 if year = 1988

-  totrain. total employees trained

-  hrsemp. tothrs/totrain

-  lscrap. log(scrap)

-  lemploy. log(employ)

-  lsales. log(sales)

-  lrework. log(rework)

-  lhrsemp. log(1 + hrsemp)

-  lscrap\_1. lagged lscrap; missing 1987

-  grant\_1. lagged grant; assumed 0 in 1987

-  clscrap. lscrap - lscrap\_1; year > 1987

-  cgrant. grant - grant\_1

-  clemploy. lemploy - lemploy[\_n-1]

-  clsales. lavgsal - lavgsal[\_n-1]

-  lavgsal. log(avgsal)

-  clavgsal. lavgsal - lavgsal[\_n-1]

-  cgrant\_1. cgrant[\_n-1]

-  chrsemp. hrsemp - hrsemp[\_n-1]

-  clhrsemp. lhrsemp - lhrsemp[\_n-1]

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(jtrain)
