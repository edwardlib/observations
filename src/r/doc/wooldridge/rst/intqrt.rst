+----------+-------------------+
| intqrt   | R Documentation   |
+----------+-------------------+

intqrt
------

Description
~~~~~~~~~~~

Data loads lazily. Type data(intqrt) into the console.

Usage
~~~~~

::

    data(intqrt)

Format
~~~~~~

A data.frame with 124 rows and 23 variables:

-  r3. bond equiv. yield, 3 mo T-bill

-  r6. bond equiv. yield, 6 mo T-bill

-  r12. yield on 1 yr. bond

-  p3. price of 3 mo. T-bill

-  p6. price of 6 mo. T-bill

-  hy6. 100\*(p3 - p6[\_n-1])/p6[\_n-1])

-  hy3. r3\*(91/365)

-  spr63. r6 - r3

-  hy3\_1. hy3[\_n-1]

-  hy6\_1. hy6[\_n-1]

-  spr63\_1. spr63[\_n-1]

-  hy6hy3\_1. hy6 - hy3\_1

-  cr3. r3 - r3\_1

-  r3\_1. r3[\_n-1]

-  chy6. hy6 - hy6\_1

-  chy3. hy3 - hy3\_1

-  chy6\_1. chy6[\_n-1]

-  chy3\_1. chy3[\_n-1]

-  cr6. r6 - r6\_1

-  cr6\_1. cr6[\_n-1]

-  cr3\_1. cr3[\_n-1]

-  r6\_1. r6[\_n-1]

-  cspr63. spr63 - spr63\_1

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(intqrt)
