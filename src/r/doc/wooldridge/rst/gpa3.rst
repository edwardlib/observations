+--------+-------------------+
| gpa3   | R Documentation   |
+--------+-------------------+

gpa3
----

Description
~~~~~~~~~~~

Data loads lazily. Type data(gpa3) into the console.

Usage
~~~~~

::

    data(gpa3)

Format
~~~~~~

A data.frame with 732 rows and 23 variables:

-  term. fall = 1, spring = 2

-  sat. SAT score

-  tothrs. total hours prior to term

-  cumgpa. cumulative GPA

-  season. =1 if in season

-  frstsem. =1 if student's 1st semester

-  crsgpa. weighted course GPA

-  verbmath. verbal SAT to math SAT ratio

-  trmgpa. term GPA

-  hssize. size h.s. grad. class

-  hsrank. rank in h.s. class

-  id. student identifier

-  spring. =1 if spring term

-  female. =1 if female

-  black. =1 if black

-  white. =1 if white

-  ctrmgpa. change in trmgpa

-  ctothrs. change in total hours

-  ccrsgpa. change in crsgpa

-  ccrspop. change in crspop

-  cseason. change in season

-  hsperc. percentile in h.s.

-  football. =1 if football player

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(gpa3)
