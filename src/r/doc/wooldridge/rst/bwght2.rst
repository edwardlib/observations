+----------+-------------------+
| bwght2   | R Documentation   |
+----------+-------------------+

bwght2
------

Description
~~~~~~~~~~~

Data loads lazily. Type data(bwght2) into the console.

Usage
~~~~~

::

    data(bwght2)

Format
~~~~~~

A data.frame with 1832 rows and 23 variables:

-  mage. mother's age, years

-  meduc. mother's educ, years

-  monpre. month prenatal care began

-  npvis. total number of prenatal visits

-  fage. father's age, years

-  feduc. father's educ, years

-  bwght. birth weight, grams

-  omaps. one minute apgar score

-  fmaps. five minute apgar score

-  cigs. avg cigarettes per day

-  drink. avg drinks per week

-  lbw. =1 if bwght <= 2000

-  vlbw. =1 if bwght <= 1500

-  male. =1 if baby male

-  mwhte. =1 if mother white

-  mblck. =1 if mother black

-  moth. =1 if mother is other

-  fwhte. =1 if father white

-  fblck. =1 if father black

-  foth. =1 if father is other

-  lbwght. log(bwght)

-  magesq. mage^2

-  npvissq. npvis^2

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(bwght2)
