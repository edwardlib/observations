+--------+-------------------+
| mroz   | R Documentation   |
+--------+-------------------+

mroz
----

Description
~~~~~~~~~~~

Data loads lazily. Type data(mroz) into the console.

Usage
~~~~~

::

    data(mroz)

Format
~~~~~~

A data.frame with 753 rows and 22 variables:

-  inlf. =1 if in lab frce, 1975

-  hours. hours worked, 1975

-  kidslt6. # kids < 6 years

-  kidsge6. # kids 6-18

-  age. woman's age in yrs

-  educ. years of schooling

-  wage. est. wage from earn, hrs

-  repwage. rep. wage at interview in 1976

-  hushrs. hours worked by husband, 1975

-  husage. husband's age

-  huseduc. husband's years of schooling

-  huswage. husband's hourly wage, 1975

-  faminc. family income, 1975

-  mtr. fed. marg. tax rte facing woman

-  motheduc. mother's years of schooling

-  fatheduc. father's years of schooling

-  unem. unem. rate in county of resid.

-  city. =1 if live in SMSA

-  exper. actual labor mkt exper

-  nwifeinc. (faminc - wage\*hours)/1000

-  lwage. log(wage)

-  expersq. exper^2

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(mroz)
