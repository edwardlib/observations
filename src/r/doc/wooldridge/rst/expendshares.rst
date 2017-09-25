+----------------+-------------------+
| expendshares   | R Documentation   |
+----------------+-------------------+

expendshares
------------

Description
~~~~~~~~~~~

Data loads lazily. Type data(expendshares) into the console.

Usage
~~~~~

::

    data(expendshares)

Format
~~~~~~

A data.frame with 1519 rows and 13 variables:

-  sfood. share of food expenditures (out of total)

-  sfuel. share of fuel expenditures

-  sclothes. share of clothing expenditures

-  salcohol. share of alcohol expenditures

-  stransport. share of transportation expenditures

-  sother. share of other expenditures

-  totexpend. total expenditure, British pounds per week

-  income. family income, British pounds per week

-  age. age of household head

-  kids. number of children: 1 or 2

-  ltotexpend. log(totexpend)

-  lincome. log(income)

-  agesq. age^2

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(expendshares)
