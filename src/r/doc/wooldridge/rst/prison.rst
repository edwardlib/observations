+----------+-------------------+
| prison   | R Documentation   |
+----------+-------------------+

prison
------

Description
~~~~~~~~~~~

Data loads lazily. Type data(prison) into the console.

Usage
~~~~~

::

    data(prison)

Format
~~~~~~

A data.frame with 714 rows and 45 variables:

-  state. alphabetical; DC = 9

-  year. 80 to 93

-  govelec. =1 if gubernatorial election

-  black. proportion black

-  metro. proportion in metro. areas

-  unem. proportion unemployed

-  criv. viol. crimes per 100,000

-  crip. prop. crimes per 100,000

-  lcriv. log(criv)

-  lcrip. log(crip)

-  gcriv. lcriv - lcriv\_1

-  gcrip. lcrip - lcrip\_1

-  y81. =1 if year == 81

-  y82.

-  y83.

-  y84.

-  y85.

-  y86.

-  y87.

-  y88.

-  y89.

-  y90.

-  y91.

-  y92.

-  y93.

-  ag0\_14. prop. pop. 0 to 14 yrs

-  ag15\_17. prop. pop. 15 to 17 yrs

-  ag18\_24. prop. pop. 18 to 24 yrs

-  ag25\_34. prop. pop. 25 to 34 yrs

-  incpc. per capita income, nominal

-  polpc. police per 100,000 residents

-  gincpc. log(incpc) - log(incpc\_1)

-  gpolpc. lpolpc - lpolpc\_1

-  cag0\_14. change in ag0\_14

-  cag15\_17. change in ag15\_17

-  cag18\_24. change in ag18\_24

-  cag25\_34. change in ag25\_34

-  cunem. change in unem

-  cblack. change in black

-  cmetro. change in metro

-  pris. prison pop. per 100,000

-  lpris. log(pris)

-  gpris. lpris - lpris[\_n-1]

-  final1. =1 if fnl dec on litig, curr yr

-  final2. =1 if dec on litig, prev 2 yrs

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(prison)
