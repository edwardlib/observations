+------------+-------------------+
| traffic1   | R Documentation   |
+------------+-------------------+

traffic1
--------

Description
~~~~~~~~~~~

Data loads lazily. Type data(traffic1) into the console.

Usage
~~~~~

::

    data(traffic1)

Format
~~~~~~

A data.frame with 51 rows and 13 variables:

-  state.

-  admn90. =1 if admin. revoc., '90

-  admn85. =1 if admin. revoc., '85

-  open90. =1 if open cont. law, '90

-  open85. =1 if open cont. law, '85

-  dthrte90. deaths per 100 mill. miles, '90

-  dthrte85. deaths per 100 mill. miles, '85

-  speed90. =1 if 65 mph, 1990

-  speed85. =0 always

-  cdthrte. dthrte90 - dthrte85

-  cadmn. admn90 - admn85

-  copen. open90 - open85

-  cspeed. speed90 - speed85

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(traffic1)
