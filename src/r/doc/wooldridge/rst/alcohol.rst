+-----------+-------------------+
| alcohol   | R Documentation   |
+-----------+-------------------+

alcohol
-------

Description
~~~~~~~~~~~

Data loads lazily. Type data(alcohol) into the console.

Usage
~~~~~

::

    data(alcohol)

Format
~~~~~~

A data.frame with 9822 rows and 33 variables:

-  abuse. =1 if abuse alcohol

-  status. out of workforce = 1; unemployed = 2, employed = 3

-  unemrate. state unemployment rate

-  age. age in years

-  educ. years of schooling

-  married. =1 if married

-  famsize. family size

-  white. =1 if white

-  exhealth. =1 if in excellent health

-  vghealth. =1 if in very good health

-  goodhealth. =1 if in good health

-  fairhealth. =1 if in fair health

-  northeast. =1 if live in northeast

-  midwest. =1 if live in midwest

-  south. =1 if live in south

-  centcity. =1 if live in central city of MSA

-  outercity. =1 if in outer city of MSA

-  qrt1. =1 if interviewed in first quarter

-  qrt2. =1 if interviewed in second quarter

-  qrt3. =1 if interviewed in third quarter

-  beertax. state excise tax, $ per gallon

-  cigtax. state cigarette tax, cents per pack

-  ethanol. state per-capita ethanol consumption

-  mothalc. =1 if mother an alcoholic

-  fathalc. =1 if father an alcoholic

-  livealc. =1 if lived with alcoholic

-  inwf. =1 if status > 1

-  employ. =1 if employed

-  agesq. age^2

-  beertaxsq. beertax^2

-  cigtaxsq. cigtax^2

-  ethanolsq. ethanol^2

-  educsq. educ^2

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(alcohol)
