+-----------+-------------------+
| pntsprd   | R Documentation   |
+-----------+-------------------+

pntsprd
-------

Description
~~~~~~~~~~~

Data loads lazily. Type data(pntsprd) into the console.

Usage
~~~~~

::

    data(pntsprd)

Format
~~~~~~

A data.frame with 553 rows and 12 variables:

-  favscr. favored team's score

-  undscr. underdog's score

-  spread. las vegas spread

-  favhome. =1 if favored team at home

-  neutral. =1 if neutral site

-  fav25. =1 if favored team in top 25

-  und25. =1 if underdog in top 25

-  fregion. favorite's region of country

-  uregion. underdog's region of country

-  scrdiff. favscr - undscr

-  sprdcvr. =1 if spread covered

-  favwin. =1 if favored team wins

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(pntsprd)
