+-----------+-------------------+
| jtrain3   | R Documentation   |
+-----------+-------------------+

jtrain3
-------

Description
~~~~~~~~~~~

Data loads lazily. Type data(jtrain3) into the console.

Usage
~~~~~

::

    data(jtrain3)

Format
~~~~~~

A data.frame with 2675 rows and 20 variables:

-  train. =1 if in job training

-  age. in years, 1977

-  educ. years of schooling

-  black. =1 if black

-  hisp. =1 if Hispanic

-  married. =1 if married

-  re74. '74 earnings, $1000s '82

-  re75. '75 earnings, $1000s '82

-  unem75. =1 if unem. all of '75

-  unem74. =1 if unem. all of '74

-  re78. '78 earnings, $1000s '82

-  agesq. age^2

-  trre74. train\*re74

-  trre75. train\*re75

-  trun74. train\*unem74

-  trun75. train\*unem75

-  avgre. (re74 + re75)/2

-  travgre. train\*avgre

-  unem78. =1 if unem. all of '78

-  em78. 1 - unem78

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(jtrain3)
