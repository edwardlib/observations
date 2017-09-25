+----------+-------------------+
| crime1   | R Documentation   |
+----------+-------------------+

crime1
------

Description
~~~~~~~~~~~

Data loads lazily. Type data(crime1) into the console.

Usage
~~~~~

::

    data(crime1)

Format
~~~~~~

A data.frame with 2725 rows and 16 variables:

-  narr86. # times arrested, 1986

-  nfarr86. # felony arrests, 1986

-  nparr86. # property crme arr., 1986

-  pcnv. proportion of prior convictions

-  avgsen. avg sentence length, mos.

-  tottime. time in prison since 18 (mos.)

-  ptime86. mos. in prison during 1986

-  qemp86. # quarters employed, 1986

-  inc86. legal income, 1986, $100s

-  durat. recent unemp duration

-  black. =1 if black

-  hispan. =1 if Hispanic

-  born60. =1 if born in 1960

-  pcnvsq. pcnv^2

-  pt86sq. ptime86^2

-  inc86sq. inc86^2

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(crime1)
