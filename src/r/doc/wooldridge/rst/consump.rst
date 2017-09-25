+-----------+-------------------+
| consump   | R Documentation   |
+-----------+-------------------+

consump
-------

Description
~~~~~~~~~~~

Data loads lazily. Type data(consump) into the console.

Usage
~~~~~

::

    data(consump)

Format
~~~~~~

A data.frame with 37 rows and 24 variables:

-  year. 1959-1995

-  i3. 3 mo. T-bill rate

-  inf. inflation rate; CPI

-  rdisp. disp. inc., 1992 $, bils.

-  rnondc. nondur. cons., 1992 $, bils.

-  rserv. services, 1992 $, bils.

-  pop. population, 1000s

-  y. per capita real disp. inc.

-  rcons. rnondc + rserv

-  c. per capita real cons.

-  r3. i3 - inf; real ex post int.

-  lc. log(c)

-  ly. log(y)

-  gc. lc - lc[\_n-1]

-  gy. ly - ly[\_n-1]

-  gc\_1. gc[\_n-1]

-  gy\_1. gy[\_n-1]

-  r3\_1. r3[\_n-1]

-  lc\_ly. lc - ly

-  lc\_ly\_1. lc\_ly[\_n-1]

-  gc\_2. gc[\_n-2]

-  gy\_2. gy[\_n-2]

-  r3\_2. r3[\_n-2]

-  lc\_ly\_2. lc\_ly[\_n-2]

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(consump)
