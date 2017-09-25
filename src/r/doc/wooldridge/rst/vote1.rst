+---------+-------------------+
| vote1   | R Documentation   |
+---------+-------------------+

vote1
-----

Description
~~~~~~~~~~~

Data loads lazily. Type data(vote1) into the console.

Usage
~~~~~

::

    data(vote1)

Format
~~~~~~

A data.frame with 173 rows and 10 variables:

-  state. state postal code

-  district. congressional district

-  democA. =1 if A is democrat

-  voteA. percent vote for A

-  expendA. camp. expends. by A, $1000s

-  expendB. camp. expends. by B, $1000s

-  prtystrA. percent vote for president

-  lexpendA. log(expendA)

-  lexpendB. log(expendB)

-  shareA. 100\*(expendA/(expendA+expendB))

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(vote1)
