+------------+-------------------+
| prminwge   | R Documentation   |
+------------+-------------------+

prminwge
--------

Description
~~~~~~~~~~~

Data loads lazily. Type data(prminwge) into the console.

Usage
~~~~~

::

    data(prminwge)

Format
~~~~~~

A data.frame with 38 rows and 25 variables:

-  year. 1950-1987

-  avgmin. weighted avg min wge, 44 indust

-  avgwage. wghted avg hrly wge, 44 indust

-  kaitz. Kaitz min wage index

-  avgcov. wghted avg coverage, 8 indust

-  covt. economy-wide coverage of min wg

-  mfgwage. avg manuf. wage

-  prdef. Puerto Rican price deflator

-  prepop. PR employ/popul ratio

-  prepopf. PR employ/popul ratio, alter.

-  prgnp. PR GNP

-  prunemp. PR unemployment rate

-  usgnp. US GNP

-  t. time trend: 1 to 38

-  post74. time trend: starts in 1974

-  lprunemp. log(prunemp)

-  lprgnp. log(prgnp)

-  lusgnp. log(usgnp)

-  lkaitz. log(kaitz)

-  lprun\_1. lprunemp[\_n-1]

-  lprepop. log(prepop)

-  lprep\_1. lprepop[\_n-1]

-  mincov. (avgmin/avgwage)\*avgcov

-  lmincov. log(mincov)

-  lavgmin. log(avgmin)

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(prminwge)
