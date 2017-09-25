+----------+-------------------+
| meap01   | R Documentation   |
+----------+-------------------+

meap01
------

Description
~~~~~~~~~~~

Data loads lazily. Type data(meap01) into the console.

Usage
~~~~~

::

    data(meap01)

Format
~~~~~~

A data.frame with 1823 rows and 11 variables:

-  dcode. district code

-  bcode. building code

-  math4. percent students satisfactory, 4th grade math

-  read4. percent students satisfactory, 4th grade reading

-  lunch. percent students eligible for free or reduced lunch

-  enroll. school enrollment

-  expend. total spending, $

-  exppp. expenditures per pupil: expend/enroll

-  lenroll. log(enroll)

-  lexpend. log(expend)

-  lexppp. log(exppp)

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(meap01)
