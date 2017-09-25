+-----------+-------------------+
| pension   | R Documentation   |
+-----------+-------------------+

pension
-------

Description
~~~~~~~~~~~

Data loads lazily. Type data(pension) into the console.

Usage
~~~~~

::

    data(pension)

Format
~~~~~~

A data.frame with 194 rows and 19 variables:

-  id. family identifier

-  pyears. years in pension plan

-  prftshr. =1 if profit sharing plan

-  choice. =1 if can choose method invest

-  female. =1 if female

-  married. =1 if married

-  age. age in years

-  educ. highest grade completed

-  finc25. $15,000 < faminc92 <= $25,000

-  finc35. $25,000 < faminc92 <= $35,000

-  finc50. $35,000 < faminc92 <= $50,000

-  finc75. $50,000 < faminc92 <= $75,000

-  finc100. $75,000 < faminc92 <= $100,000

-  finc101. $100,000 < faminc92

-  wealth89. net worth, 1989, $1000

-  black. =1 if black

-  stckin89. =1 if owned stock in 1989

-  irain89. =1 if had IRA in 1989

-  pctstck. 0=mstbnds,50=mixed,100=mststcks

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(pension)
