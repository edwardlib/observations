+---------+-------------------+
| cps91   | R Documentation   |
+---------+-------------------+

cps91
-----

Description
~~~~~~~~~~~

Data loads lazily. Type data(cps91) into the console.

Usage
~~~~~

::

    data(cps91)

Format
~~~~~~

A data.frame with 5634 rows and 24 variables:

-  husage. husband's age

-  husunion. =1 if hus. in union

-  husearns. hus. weekly earns

-  huseduc. husband's yrs schooling

-  husblck. =1 if hus. black

-  hushisp. =1 if hus. hispanic

-  hushrs. hus. weekly hours

-  kidge6. =1 if have child >= 6

-  earns. wife's weekly earnings

-  age. wife's age

-  black. =1 if wife black

-  educ. wife's yrs schooling

-  hispanic. =1 if wife hispanic

-  union. =1 if wife in union

-  faminc. annual family income

-  husexp. huseduc - husage - 6

-  exper. age - educ - 6

-  kidlt6. =1 if have child < 6

-  hours. wife's weekly hours

-  expersq. exper^2

-  nwifeinc. non-wife inc, $1000s

-  inlf. =1 if wife in labor force

-  hrwage. earns/hours

-  lwage. log(hrwage)

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(cps91)
