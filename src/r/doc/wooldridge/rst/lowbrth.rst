+-----------+-------------------+
| lowbrth   | R Documentation   |
+-----------+-------------------+

lowbrth
-------

Description
~~~~~~~~~~~

Data loads lazily. Type data(lowbrth) into the console.

Usage
~~~~~

::

    data(lowbrth)

Format
~~~~~~

A data.frame with 100 rows and 36 variables:

-  year. 1987 or 1990

-  lowbrth. perc births low weight

-  infmort. infant mortality rate

-  afdcprt. # participants in AFDC, 1000s

-  popul. population, 1000s

-  pcinc. per capita income

-  physic. # physicians, 1000s

-  afdcprc. percent of pop in AFDC

-  d90. =1 if year == 1990

-  lpcinc. log of pcinc

-  cafdcprc. change in afdcprc

-  clpcinc. change in lpcinc

-  lphysic. log of physic

-  clphysic. change in lphysic

-  clowbrth. change in lowbrth

-  cinfmort. change in infmort

-  afdcpay. avg monthly AFDC payment

-  afdcinc. afdcpay as percent pcinc

-  lafdcpay. log of afdcpay

-  clafdcpy. change in lafdcpay

-  cafdcinc. change in afdcinc

-  stateabb. state postal code

-  state. name of state

-  beds. # hospital beds, 1000s

-  bedspc. beds per capita

-  lbedspc. log(bedspc)

-  clbedspc. change in lbedspc

-  povrate. percent people below poverty line

-  cpovrate. change in povrate

-  afdcpsq. afdcper^2

-  cafdcpsq. change in afdcpsq

-  physicpc. physicians per capita

-  lphypc. log(physicpc)

-  clphypc. change in lphypc

-  lpopul. log(popul)

-  clpopul. change in lpopul

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(lowbrth)
