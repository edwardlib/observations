+--------+-------------------+
| fish   | R Documentation   |
+--------+-------------------+

fish
----

Description
~~~~~~~~~~~

Data loads lazily. Type data(fish) into the console.

Usage
~~~~~

::

    data(fish)

Format
~~~~~~

A data.frame with 97 rows and 20 variables:

-  prca. price for Asian buyers

-  prcw. price for white buyers

-  qtya. quantity sold to Asians

-  qtyw. quantity sold to whites

-  mon. =1 if Monday

-  tues. =1 if Tuesday

-  wed. =1 if Wednesday

-  thurs. =1 if Thursday

-  speed2. min past 2 days wind speeds

-  wave2. avg max last 2 days wave height

-  speed3. 3 day lagged max windspeed

-  wave3. avg max wave hghts of 3 & 4 day lagged hghts

-  avgprc. ((prca\*qtya) + (prcw\*qtyw))/(qtya + qtyw)

-  totqty. qtya + qtyw

-  lavgprc. log(avgprc)

-  ltotqty. log(totqty)

-  t. time trend

-  lavgp\_1. lavgprc[\_n-1]

-  gavgprc. lavgprc - lavgp\_1

-  gavgp\_1. gavgprc[\_n-1]

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(fish)
