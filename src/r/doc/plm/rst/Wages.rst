+---------+-------------------+
| Wages   | R Documentation   |
+---------+-------------------+

Panel Data of Individual Wages
------------------------------

Description
~~~~~~~~~~~

| A panel of 595 individuals from 1976 to 1982, taken from the Panel
  Study of Income Dynamics (PSID).
| The data are organized as a stacked time series/balanced panel, see
  **Examples** on how to convert to a ``pdata.frame``.

*total number of observations* : 4165

*observation* : individuals

*country* : United States

Usage
~~~~~

::

    data(Wages)

Format
~~~~~~

A data frame containing:

exp
    years of full-time work experience.

wks
    weeks worked.

bluecol
    blue collar?

ind
    works in a manufacturing industry?

south
    resides in the south?

smsa
    resides in a standard metropolitan statistical area?

married
    married?

sex
    a factor with levels ``"male"`` and ``"female"``

union
    individual's wage set by a union contract?

ed
    years of education.

black
    is the individual black?

lwage
    logarithm of wage.

Source
~~~~~~

Online complements to Baltagi (2001):

http://www.wiley.com/legacy/wileychi/baltagi/

Online complements to Baltagi (2013):

http://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=4338&itemId=1118672321&resourceId=13452

References
~~~~~~~~~~

Baltagi, Badi H. (2001) *Econometric Analysis of Panel Data*, 2nd ed.,
John Wiley and Sons.

Baltagi, Badi H. (2013) *Econometric Analysis of Panel Data*, 5th ed.,
John Wiley and Sons.

Cornwell, C. and P. Rupert (1988) “Efficient estimation with panel data:
an empirical comparison of instrumental variables estimators”, *Journal
of Applied Econometrics*, **3**\ (2), pp. 149–155.

Examples
~~~~~~~~

::

    # data set 'Wages' is organized as a stacked time series/balanced panel
    data("Wages", package = "plm")
    Wag <- pdata.frame(Wages, index=595)
