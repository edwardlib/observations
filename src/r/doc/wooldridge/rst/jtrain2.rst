+-----------+-------------------+
| jtrain2   | R Documentation   |
+-----------+-------------------+

jtrain2
-------

Description
~~~~~~~~~~~

Data loads lazily. Type data(jtrain2) into the console.

Usage
~~~~~

::

    data(jtrain2)

Format
~~~~~~

A data.frame with 445 rows and 19 variables:

-  train. =1 if assigned to job training

-  age. age in 1977

-  educ. years of education

-  black. =1 if black

-  hisp. =1 if Hispanic

-  married. =1 if married

-  nodegree. =1 if no high school degree

-  mosinex. # mnths prior to 1/78 in expmnt

-  re74. real earns., 1974, $1000s

-  re75. real earns., 1975, $1000s

-  re78. real earns., 1978, $1000s

-  unem74. =1 if unem. all of 1974

-  unem75. =1 if unem. all of 1975

-  unem78. =1 if unem. all of 1978

-  lre74. log(re74); zero if re74 == 0

-  lre75. log(re75); zero if re75 == 0

-  lre78. log(re78); zero if re78 == 0

-  agesq. age^2

-  mostrn. months in training

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(jtrain2)
