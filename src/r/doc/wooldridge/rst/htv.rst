+-------+-------------------+
| htv   | R Documentation   |
+-------+-------------------+

htv
---

Description
~~~~~~~~~~~

Data loads lazily. Type data(htv) into the console.

Usage
~~~~~

::

    data(htv)

Format
~~~~~~

A data.frame with 1230 rows and 23 variables:

-  wage. hourly wage, 1991

-  abil. abil. measure, not standardized

-  educ. highest grade completed by 1991

-  ne. =1 if in northeast, 1991

-  nc. =1 if in nrthcntrl, 1991

-  west. =1 if in west, 1991

-  south. =1 if in south, 1991

-  exper. potential experience

-  motheduc. highest grade, mother

-  fatheduc. highest grade, father

-  brkhme14. =1 if broken home, age 14

-  sibs. number of siblings

-  urban. =1 if in urban area, 1991

-  ne18. =1 if in NE, age 18

-  nc18. =1 if in NC, age 18

-  south18. =1 if in south, age 18

-  west18. =1 if in west, age 18

-  urban18. =1 if in urban area, age 18

-  tuit17. college tuition, age 17

-  tuit18. college tuition, age 18

-  lwage. log(wage)

-  expersq. exper^2

-  ctuit. tuit18 - tuit17

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(htv)
