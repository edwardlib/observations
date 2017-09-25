+------------+-------------------+
| benefits   | R Documentation   |
+------------+-------------------+

benefits
--------

Description
~~~~~~~~~~~

Data loads lazily. Type data(benefits) into the console.

Usage
~~~~~

::

    data(benefits)

Format
~~~~~~

A data.frame with 1848 rows and 18 variables:

-  distid. district identifier

-  schid. school identifier

-  lunch. percent eligible, free lunch

-  enroll. school enrollment

-  staff. staff per 1000 students

-  exppp. expenditures per pupil

-  avgsal. average teacher salary, $

-  avgben. average teacher non-salary benefits, $

-  math4. percent passing 4th grade math test

-  story4. percent passing 4th grade reading test

-  bs. avgben/avgsal

-  lavgsal. log(avgsal)

-  lenroll. log(enroll)

-  lstaff. log(staff)

-  bsbar. within-district avg of bs

-  lunchbar. within-district avg of lunch

-  lenrollbar. within-district avg of lenroll

-  lstaffbar. within-district avg of lstaff

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(benefits)
