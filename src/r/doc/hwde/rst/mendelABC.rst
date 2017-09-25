+-------------+-------------------+
| mendelABC   | R Documentation   |
+-------------+-------------------+

Mendel's F2 trifactorial data

Description
~~~~~~~~~~~

The ``mendel3`` data frame has 27 rows and 4 columns. Data are from
Mendel (1886), and are reproduced in Fisher (1936) and Weir (1996).

ABC:
Seed Shape      (A: round or wrinkled)
Cotyledon Color (B: albumen yellow or green)
Seed Coat Color (C: grey-brown or white)


Usage
~~~~~

::

    data(mendelABC)

Format
~~~~~~

This data frame contains the following columns:

seedshape
    Factor with levels: ``AA``, ``Aa`` and ``aa``

cotylcolor
    Factor with levels: ``BB``, ``Bb`` and ``bb``

coatcolor
    Factor with levels: ``CC``, ``Cc`` and ``cc``

Observed
    a numeric vector that holds the frequencies.

Details
~~~~~~~

The data are reviewed in detail in Fisher (1936). For a brief
discussion, and references to work that revisits Fisher's conclusions,
see Weir (1996).

Source
~~~~~~

Data are from Mendel (1886), and are reproduced in Fisher (1936) and
Weir (1996).

References
~~~~~~~~~~

1. Fisher, R.A. 1936. Has Mendel's work been rediscovered? *Annals of
Science* **1**:115-137.

2. Mendel, G. 1886. Versuche uber Pflanzen-Hybriden. Verhandlugen des
Naturforschenden Vereines in Brunn **4**:3-47. (An English translation.
with annotations, is available from
http://www.esp.org/foundations/genetics/classical/gm-65.pdf NB also the
English translation by Royal Horticultural Society of London, reprinted
in Peters, J.A. 1959. *Classic Papers in Genetics.* Prentice-Hall.)

3. Weir, B.S. 1996. *Genetic Data Analysis II.* Sinauer.

Examples
~~~~~~~~

::

    ## Lay table out as a 3D array, as in Fisher (1936)
    abc <- aperm(array(mendelABC[,4], dim=c(3,3,3)), c(1,3,2))
    dimnames(abc) <- list(B=c('BB','Bb','bb'), 
                          A=c('AA','Aa','aa'),
                          C=c('CC','Cc','cc'))
    abc
    ## Fit Hardy-Weinberg disequilibium model
    hwde(mendelABC, loci=c("seedshape","cotylcolor","coatcolor"))
