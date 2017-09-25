+----------+-------------------+
| barium   | R Documentation   |
+----------+-------------------+

barium
------

Description
~~~~~~~~~~~

Data loads lazily. Type data(barium) into the console.

Usage
~~~~~

::

    data(barium)

Format
~~~~~~

A data.frame with 131 rows and 31 variables:

-  chnimp. Chinese imports, bar. chl.

-  bchlimp. total imports bar. chl.

-  befile6. =1 for all 6 mos before filing

-  affile6. =1 for all 6 mos after filing

-  afdec6. =1 for all 6 mos after decision

-  befile12. =1 all 12 mos before filing

-  affile12. =1 all 12 mos after filing

-  afdec12. =1 all 12 mos after decision

-  chempi. chemical production index

-  gas. gasoline production

-  rtwex. exchange rate index

-  spr. =1 for spring months

-  sum. =1 for summer months

-  fall. =1 for fall months

-  lchnimp. log(chnimp)

-  lgas. log(gas)

-  lrtwex. log(rtwex)

-  lchempi. log(chempi)

-  t. time trend

-  feb. =1 if month is feb

-  mar. =1 if month is march

-  apr.

-  may.

-  jun.

-  jul.

-  aug.

-  sep.

-  oct.

-  nov.

-  dec.

-  percchn. percent imports from china

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(barium)
