+----------+-------------------+
| meap93   | R Documentation   |
+----------+-------------------+

meap93
------

Description
~~~~~~~~~~~

Data loads lazily. Type data(meap93) into the console.

Usage
~~~~~

::

    data(meap93)

Format
~~~~~~

A data.frame with 408 rows and 17 variables:

-  lnchprg. perc of studs in sch lnch prog

-  enroll. school enrollment

-  staff. staff per 1000 students

-  expend. expend. per stud, $

-  salary. avg. teacher salary, $

-  benefits. avg. teacher benefits, $

-  droprate. school dropout rate, perc

-  gradrate. school graduation rate, perc

-  math10. perc studs passing MEAP math

-  sci11. perc studs passing MEAP science

-  totcomp. salary + benefits

-  ltotcomp. log(totcomp)

-  lexpend. log of expend

-  lenroll. log(enroll)

-  lstaff. log(staff)

-  bensal. benefits/salary

-  lsalary. log(salary)

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(meap93)
