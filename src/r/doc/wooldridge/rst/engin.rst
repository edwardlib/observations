+---------+-------------------+
| engin   | R Documentation   |
+---------+-------------------+

engin
-----

Description
~~~~~~~~~~~

Data loads lazily. Type data(engin) into the console.

Usage
~~~~~

::

    data(engin)

Format
~~~~~~

A data.frame with 403 rows and 17 variables:

-  male. =1 if male

-  educ. highest grade completed

-  wage. monthly salary, Thai baht

-  swage. starting wage

-  exper. years on current job

-  pexper. previous experience

-  lwage. log(wage)

-  expersq. exper^2

-  highgrad. =1 if high school graduate

-  college. =1 if college graduate

-  grad. =1 if some graduate school

-  polytech. =1 if a polytech

-  highdrop. =1 if no high school degree

-  lswage. log(swage)

-  pexpersq. pexper^2

-  mleeduc. male\*educ

-  mleeduc0. male\*(educ - 14)

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(engin)
