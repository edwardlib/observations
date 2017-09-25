+----------+-------------------+
| crime4   | R Documentation   |
+----------+-------------------+

crime4
------

Description
~~~~~~~~~~~

Data loads lazily. Type data(crime4) into the console.

Usage
~~~~~

::

    data(crime4)

Format
~~~~~~

A data.frame with 630 rows and 59 variables:

-  county. county identifier

-  year. 81 to 87

-  crmrte. crimes committed per person

-  prbarr. 'probability' of arrest

-  prbconv. 'probability' of conviction

-  prbpris. 'probability' of prison sentenc

-  avgsen. avg. sentence, days

-  polpc. police per capita

-  density. people per sq. mile

-  taxpc. tax revenue per capita

-  west. =1 if in western N.C.

-  central. =1 if in central N.C.

-  urban. =1 if in SMSA

-  pctmin80. perc. minority, 1980

-  wcon. weekly wage, construction

-  wtuc. wkly wge, trns, util, commun

-  wtrd. wkly wge, whlesle, retail trade

-  wfir. wkly wge, fin, ins, real est

-  wser. wkly wge, service industry

-  wmfg. wkly wge, manufacturing

-  wfed. wkly wge, fed employees

-  wsta. wkly wge, state employees

-  wloc. wkly wge, local gov emps

-  mix. offense mix: face-to-face/other

-  pctymle. percent young male

-  d82. =1 if year == 82

-  d83. =1 if year == 83

-  d84. =1 if year == 84

-  d85. =1 if year == 85

-  d86. =1 if year == 86

-  d87. =1 if year == 87

-  lcrmrte. log(crmrte)

-  lprbarr. log(prbarr)

-  lprbconv. log(prbconv)

-  lprbpris. log(prbpris)

-  lavgsen. log(avgsen)

-  lpolpc. log(polpc)

-  ldensity. log(density)

-  ltaxpc. log(taxpc)

-  lwcon. log(wcon)

-  lwtuc. log(wtuc)

-  lwtrd. log(wtrd)

-  lwfir. log(wfir)

-  lwser. log(wser)

-  lwmfg. log(wmfg)

-  lwfed. log(wfed)

-  lwsta. log(wsta)

-  lwloc. log(wloc)

-  lmix. log(mix)

-  lpctymle. log(pctymle)

-  lpctmin. log(pctmin)

-  clcrmrte. lcrmrte - lcrmrte[\_n-1]

-  clprbarr. lprbarr - lprbarr[\_n-1]

-  clprbcon. lprbconv - lprbconv[\_n-1]

-  clprbpri. lprbpri - lprbpri[t-1]

-  clavgsen. lavgsen - lavgsen[t-1]

-  clpolpc. lpolpc - lpolpc[t-1]

-  cltaxpc. ltaxpc - ltaxpc[t-1]

-  clmix. lmix - lmix[t-1]

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(crime4)
