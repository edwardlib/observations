+----------+-------------------+
| nbasal   | R Documentation   |
+----------+-------------------+

nbasal
------

Description
~~~~~~~~~~~

Data loads lazily. Type data(nbasal) into the console.

Usage
~~~~~

::

    data(nbasal)

Format
~~~~~~

A data.frame with 269 rows and 22 variables:

-  marr. =1 if married

-  wage. annual salary, thousands $

-  exper. years as professional player

-  age. age in years

-  coll. years played in college

-  games. average games per year

-  minutes. average minutes per year

-  guard. =1 if guard

-  forward. =1 if forward

-  center. =1 if center

-  points. points per game

-  rebounds. rebounds per game

-  assists. assists per game

-  draft. draft number

-  allstar. =1 if ever all star

-  avgmin. minutes per game

-  lwage. log(wage)

-  black. =1 if black

-  children. =1 if has children

-  expersq. exper^2

-  agesq. age^2

-  marrblck. marr\*black

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(nbasal)
