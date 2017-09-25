+-----------+-------------------+
| affairs   | R Documentation   |
+-----------+-------------------+

affairs
-------

Description
~~~~~~~~~~~

Data loads lazily. Type data(affairs) into the console.

Usage
~~~~~

::

    data(affairs)

Format
~~~~~~

A data.frame with 601 rows and 19 variables:

-  id. identifier

-  male. =1 if male

-  age. in years

-  yrsmarr. years married

-  kids. =1 if have kids

-  relig. 5 = very relig., 4 = somewhat, 3 = slightly, 2 = not at all, 1
   = anti

-  educ. years schooling

-  occup. occupation, reverse Hollingshead scale

-  ratemarr. 5 = vry hap marr, 4 = hap than avg, 3 = avg, 2 = smewht
   unhap, 1 = vry unhap

-  naffairs. number of affairs within last year

-  affair. =1 if had at least one affair

-  vryhap. ratemarr == 5

-  hapavg. ratemarr == 4

-  avgmarr. ratemarr == 3

-  unhap. ratemarr == 2

-  vryrel. relig == 5

-  smerel. relig == 4

-  slghtrel. relig == 3

-  notrel. relig == 2

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(affairs)
