+----------+-------------------+
| infmrt   | R Documentation   |
+----------+-------------------+

infmrt
------

Description
~~~~~~~~~~~

Data loads lazily. Type data(infmrt) into the console.

Usage
~~~~~

::

    data(infmrt)

Format
~~~~~~

A data.frame with 102 rows and 12 variables:

-  year. 1987 or 1990

-  infmort. deaths per 1,000 live births

-  afdcprt. afdc partic., 1000s

-  popul. population, 1000s

-  pcinc. per capita income

-  physic. drs. per 100,000 civilian pop.

-  afdcper. percent on AFDC

-  d90. =1 if year == 1990

-  lpcinc. log(pcinc)

-  lphysic. log(physic)

-  DC. =1 for Washington DC

-  lpopul. log(popul)

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(infmrt)
