+-----------+-------------------+
| ceosal2   | R Documentation   |
+-----------+-------------------+

ceosal2
-------

Description
~~~~~~~~~~~

Data loads lazily. Type data(ceosal2) into the console.

Usage
~~~~~

::

    data(ceosal2)

Format
~~~~~~

A data.frame with 177 rows and 15 variables:

-  salary. 1990 compensation, $1000s

-  age. in years

-  college. =1 if attended college

-  grad. =1 if attended graduate school

-  comten. years with company

-  ceoten. years as ceo with company

-  sales. 1990 firm sales, millions

-  profits. 1990 profits, millions

-  mktval. market value, end 1990, mills.

-  lsalary. log(salary)

-  lsales. log(sales)

-  lmktval. log(mktval)

-  comtensq. comten^2

-  ceotensq. ceoten^2

-  profmarg. profits as percent of sales

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(ceosal2)
