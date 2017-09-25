+----------+-------------------+
| fringe   | R Documentation   |
+----------+-------------------+

fringe
------

Description
~~~~~~~~~~~

Data loads lazily. Type data(fringe) into the console.

Usage
~~~~~

::

    data(fringe)

Format
~~~~~~

A data.frame with 616 rows and 39 variables:

-  annearn. annual earnings, $

-  hrearn. hourly earnings, $

-  exper. years work experience

-  age. age in years

-  depends. number of dependents

-  married. =1 if married

-  tenure. years with current employer

-  educ. years schooling

-  nrtheast. =1 if live in northeast

-  nrthcen. =1 if live in north central

-  south. =1 if live in south

-  male. =1 if male

-  white. =1 if white

-  union. =1 if union member

-  office.

-  annhrs. annual hours worked

-  ind1. industry dummy

-  ind2.

-  ind3.

-  ind4.

-  ind5.

-  ind6.

-  ind7.

-  ind8.

-  ind9.

-  vacdays. $ value of vac. days

-  sicklve. $ value of sick leave

-  insur. $ value of employee insur

-  pension. $ value of employee pension

-  annbens. vacdays+sicklve+insur+pension

-  hrbens. hourly benefits, $

-  annhrssq. annhrs^2

-  beratio. annbens/annearn

-  lannhrs. log(annhrs)

-  tenuresq. tenure^2

-  expersq. exper^2

-  lannearn. log(annearn)

-  peratio. pension/annearn

-  vserat. (vacdays+sicklve)/annearn

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(fringe)
