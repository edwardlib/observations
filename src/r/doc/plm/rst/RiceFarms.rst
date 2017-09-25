+-------------+-------------------+
| RiceFarms   | R Documentation   |
+-------------+-------------------+

Production of Rice in India
---------------------------

Description
~~~~~~~~~~~

a panel of 171 observations

*number of observations* : 1026

*observation* : farms

*country* : Indonesia

Usage
~~~~~

::

    data(RiceFarms)

Format
~~~~~~

A dataframe containing :

id
    the farm identifier

size
    the total area cultivated with rice, measured in hectares

status
    land status, on of ``'owner'`` (non sharecroppers, owner operators
    or leaseholders or both), ``'share'`` (sharecroppers), ``'mixed'``
    (mixed of the two previous status)

varieties
    one of ``'trad'`` (traditional varieties), ``'high'`` (high yielding
    varieties) and ``'mixed'`` (mixed varieties)

bimas
    bIMAS is an intensification program; one of ``'no'`` (non-bimas
    farmer), ``'yes'`` (bimas farmer) or ``'mixed'`` (part but not all
    of farmer's land was registered to be in the bimas program)

seed
    seed in kilogram

urea
    urea in kilogram

phosphate
    phosphate in kilogram

pesticide
    pesticide cost in Rupiah

pseed
    price of seed in Rupiah per kg

purea
    price of urea in Rupiah per kg

pphosph
    price of phosphate in Rupiah per kg

hiredlabor
    hired labor in hours

famlabor
    family labor in hours

totlabor
    total labor (excluding harvest labor)

wage
    labor wage in Rupiah per hour

goutput
    gross output of rice in kg

noutput
    net output, gross output minus harvesting cost (paid in terms of
    rice)

price
    price of rough rice in Rupiah per kg

region
    one of ``'wargabinangun'``, ``'langan'``, ``'gunungwangi'``,
    ``'malausma'``, ``'sukaambit'``, ``'ciwangi'``

Source
~~~~~~

Qu Feng and William C. Horrace, (2012) “Alternative Measures of
Technical Efficiency: Skew, Bias and Scale”, *Journal of Applied
Econometrics*, **27(2)**, pp. 253–268.
