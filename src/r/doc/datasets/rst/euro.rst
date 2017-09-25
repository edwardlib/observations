+--------+-------------------+
| euro   | R Documentation   |
+--------+-------------------+

Conversion Rates of Euro Currencies
-----------------------------------

Description
~~~~~~~~~~~

Conversion rates between the various Euro currencies.

Usage
~~~~~

::

    euro
    euro.cross

Format
~~~~~~

``euro`` is a named vector of length 11, ``euro.cross`` a matrix of size
11 by 11, with dimnames.

Details
~~~~~~~

The data set ``euro`` contains the value of 1 Euro in all currencies
participating in the European monetary union (Austrian Schilling ATS,
Belgian Franc BEF, German Mark DEM, Spanish Peseta ESP, Finnish Markka
FIM, French Franc FRF, Irish Punt IEP, Italian Lira ITL, Luxembourg
Franc LUF, Dutch Guilder NLG and Portuguese Escudo PTE). These
conversion rates were fixed by the European Union on December 31, 1998.
To convert old prices to Euro prices, divide by the respective rate and
round to 2 digits.

The data set ``euro.cross`` contains conversion rates between the
various Euro currencies, i.e., the result of ``outer(1 / euro, euro)``.

Examples
~~~~~~~~

::

    cbind(euro)

    ## These relations hold:
    euro == signif(euro, 6) # [6 digit precision in Euro's definition]
    all(euro.cross == outer(1/euro, euro))

    ## Convert 20 Euro to Belgian Franc
    20 * euro["BEF"]
    ## Convert 20 Austrian Schilling to Euro
    20 / euro["ATS"]
    ## Convert 20 Spanish Pesetas to Italian Lira
    20 * euro.cross["ESP", "ITL"]

    require(graphics)
    dotchart(euro,
             main = "euro data: 1 Euro in currency unit")
    dotchart(1/euro,
             main = "euro data: 1 currency unit in Euros")
    dotchart(log(euro, 10),
             main = "euro data: log10(1 Euro in currency unit)")
